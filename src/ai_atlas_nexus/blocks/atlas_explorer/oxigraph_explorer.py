from collections import defaultdict
from typing import Any, Dict, List, Optional, Set
from urllib.parse import quote

import inflect
import pyoxigraph
from pydantic import BaseModel

from ai_atlas_nexus.blocks.atlas_explorer.base import (
    ExplorerBase,
    StarGraph,
    StarGraphComparison,
)
from ai_atlas_nexus.blocks.atlas_explorer.query_builder import (
    NEXUS_URI,
    SPARQLQueryBuilder,
)


try:
    from txtai import Embeddings
except ImportError:
    Embeddings = None


ie = inflect.engine()


class OxigraphExplorer(ExplorerBase):

    def __init__(self, data):
        """
        Initialize OxigraphExplorer by loading LinkML data into a pyoxigraph Store.

        Args:
            data: Container
                Container object, populated instance of the knowledge graph
        """
        self._data = data
        self._combined_cache = {}
        self._id_cache = {}
        self._collection_map = {}
        self._embeddings = None
        self._qb = SPARQLQueryBuilder()

        self._build_id_cache_index()
        self._build_collection_map()
        self._store = self._load_data_to_store(data)

    def _build_id_cache_index(self):
        """
        A dict which is mapping ID to LinkML obj
        """
        for class_name in self._data.model_fields_set:
            items = getattr(self._data, class_name) or []
            for item in items:
                if hasattr(item, "id") and item.id:
                    self._id_cache[item.id] = item

    def _build_collection_map(self):
        """Map collection_key → ClassName for SPARQL type filtering."""
        for field in self._data.model_fields_set:
            items = getattr(self._data, field) or []
            if items:
                self._collection_map[field] = type(items[0]).__name__

    def _check_subclasses(self, result, class_name):
        """
        Search through all collections for instances whose type name matches
        the requested class name (handles singular/plural conversion).
        """
        for field in self._data.model_fields_set:
            items = getattr(self._data, field) or []
            if not isinstance(items, list):
                items = [items]

            for instance in items:
                instance_type_name = type(instance).__name__
                possible_singular = ie.singular_noun(class_name)
                if instance_type_name.lower() == class_name.lower() or (
                    possible_singular
                    and instance_type_name.lower() == possible_singular.lower()
                ):
                    result.append(instance)

        return result

    def _load_data_to_store(self, data) -> pyoxigraph.Store:
        """
        Load Container into a pyoxigraph Store by building RDF quads from Pydantic objects.
        """
        store = pyoxigraph.Store()
        seen_iris = set()

        # Iterate all objects and add RDF quads
        for field_name in data.model_fields_set:
            items = getattr(data, field_name) or []
            if not isinstance(items, list):
                items = [items]

            for item in items:
                if not isinstance(item, BaseModel):
                    continue

                item_id = getattr(item, "id", None)
                if not item_id:
                    continue

                # URI-encode the ID to handle special characters
                encoded_id = quote(str(item_id), safe="")
                item_uri = pyoxigraph.NamedNode(f"{NEXUS_URI}{encoded_id}")

                # Skip duplicates
                if item_uri in seen_iris:
                    continue
                seen_iris.add(item_uri)

                # Add rdf:type quad
                class_name = type(item).__name__
                class_uri = pyoxigraph.NamedNode(f"{NEXUS_URI}{class_name}")
                rdf_type = pyoxigraph.NamedNode("http://www.w3.org/1999/02/22-rdf-syntax-ns#type")
                store.add(pyoxigraph.Quad(item_uri, rdf_type, class_uri, None))

                # Add property quads
                for field_name_attr, field_value in item:
                    if field_value is None or field_name_attr.startswith("_"):
                        continue

                    prop_uri = pyoxigraph.NamedNode(f"{NEXUS_URI}{field_name_attr}")

                    if isinstance(field_value, str):
                        obj = pyoxigraph.Literal(field_value)
                    elif isinstance(field_value, bool):
                        obj = pyoxigraph.Literal(str(field_value).lower(), datatype=pyoxigraph.NamedNode("http://www.w3.org/2001/XMLSchema#boolean"))
                    elif isinstance(field_value, int):
                        obj = pyoxigraph.Literal(str(field_value), datatype=pyoxigraph.NamedNode("http://www.w3.org/2001/XMLSchema#integer"))
                    elif isinstance(field_value, float):
                        obj = pyoxigraph.Literal(str(field_value), datatype=pyoxigraph.NamedNode("http://www.w3.org/2001/XMLSchema#decimal"))
                    elif isinstance(field_value, list):
                        # Add multiple quads for list values
                        for list_item in field_value:
                            if isinstance(list_item, str):
                                obj = pyoxigraph.Literal(list_item)
                                store.add(pyoxigraph.Quad(item_uri, prop_uri, obj, None))
                        continue
                    else:
                        obj = pyoxigraph.Literal(str(field_value))

                    store.add(pyoxigraph.Quad(item_uri, prop_uri, obj, None))

        return store

    def _uri_to_pydantic(self, node: pyoxigraph.NamedNode) -> Optional[Any]:
        """
        Convert a pyoxigraph NamedNode to a Pydantic object via id_cache.
        """
        from urllib.parse import unquote
        uri_str = str(node)
        # NamedNode.__str__() includes angle brackets, e.g. "<http://...>"
        if uri_str.startswith("<") and uri_str.endswith(">"):
            uri_str = uri_str[1:-1]
        if uri_str.startswith(NEXUS_URI):
            encoded_id = uri_str[len(NEXUS_URI) :]
            identifier = unquote(encoded_id)
            return self._id_cache.get(identifier)
        return None

    def _get_embeddings(self):
        """Lazy-initialize and return a txtai Embeddings instance."""
        if self._embeddings is None:
            if Embeddings is None:
                raise ImportError("txtai is required for semantic similarity. Install with: pip install txtai")
            self._embeddings = Embeddings()
        return self._embeddings

    def _compare_values(self, val_a: Any, val_b: Any, max_depth: int, threshold: float) -> float:
        """
        Compare two field values and return a similarity score (0.0-100.0).

        Handles: None, str (text or ID reference), bool/int/float (exact), list (Jaccard).
        For ID references at depth > 0, recursively compares referenced objects.
        """
        if val_a is None and val_b is None:
            return 100.0
        if val_a is None or val_b is None:
            return 0.0

        if isinstance(val_a, str) and isinstance(val_b, str):
            if val_a in self._id_cache and val_b in self._id_cache and max_depth > 0:
                obj_a = self._id_cache[val_a]
                obj_b = self._id_cache[val_b]
                prop_scores = {}
                sim = self.object_similarity(obj_a, obj_b, threshold, prop_scores, max_depth - 1)
                return 100.0 if sim >= threshold else sim

            if isinstance(val_a, str) and isinstance(val_b, str):
                try:
                    embeddings = self._get_embeddings()
                    score = embeddings.similarity(val_a, [val_b])[0][1]
                    return score * 100.0
                except Exception:
                    return 100.0 if val_a == val_b else 0.0

        if isinstance(val_a, bool) and isinstance(val_b, bool):
            return 100.0 if val_a == val_b else 0.0
        if isinstance(val_a, int) and isinstance(val_b, int):
            return 100.0 if val_a == val_b else 0.0
        if isinstance(val_a, float) and isinstance(val_b, float):
            return 100.0 if val_a == val_b else 0.0

        if isinstance(val_a, list) and isinstance(val_b, list):
            try:
                set_a = set(val_a) if val_a else set()
                set_b = set(val_b) if val_b else set()
                if not set_a and not set_b:
                    return 100.0
                intersection = len(set_a & set_b)
                union = len(set_a | set_b)
                return (intersection / union * 100.0) if union > 0 else 0.0
            except (TypeError, ValueError):
                return 0.0

        return 0.0

    def get_all_classes(self) -> List[str]:
        """
        Get all class names that have data in the knowledge graph.

        Returns:
            list[str]: List of class names
        """
        return list(self._data.model_fields_set)

    def get_all(
        self,
        class_name: Optional[str] = None,
        taxonomy: Optional[str] = None,
        vocabulary: Optional[str] = None,
        document: Optional[str] = None,
    ) -> List[Any]:
        """
        Get all instances of a specified class with optional filters.

        Args:
            class_name: str | None
                Name of the class to retrieve
            taxonomy: str | None
                (Optional) Filter by taxonomy id
            vocabulary: str | None
                (Optional) Filter by vocabulary id
            document: str | None
                (Optional) Filter by document id

        Returns:
            list: List of Pydantic instances
        """
        class_names = []

        if class_name is None:
            class_names = self.get_all_classes()
        elif isinstance(class_name, str):
            class_names.append(class_name)
        else:
            class_names = class_name

        taxonomies = []

        if taxonomy is None:
            taxonomies = ["ibm-risk-atlas"]
        elif isinstance(taxonomy, str):
            taxonomies.append(taxonomy)
        else:
            taxonomies = taxonomy

        cache_key = (
            tuple(class_names) if isinstance(class_names, list) else class_name,
            tuple(taxonomies),
            vocabulary,
            document,
        )

        if cache_key in self._combined_cache:
            return self._combined_cache[cache_key]

        result = []
        seen_ids = set()

        for key in class_names:
            # Resolve collection key from model
            if key not in self._data.model_fields_set:
                for k in self._data.model_fields_set:
                    if k.lower().replace("_", "") == key.lower().replace("_", ""):
                        key = k
                        break

            class_name_camel = self._collection_map.get(key)

            if not class_name_camel:
                # Try to find by class name (e.g., "Risk" or "Action") via _check_subclasses
                subclass_results = self._check_subclasses([], key)
                for item in subclass_results:
                    item_id = getattr(item, "id", None)
                    if item_id and item_id not in seen_ids:
                        result.append(item)
                        seen_ids.add(item_id)
                    elif not item_id:
                        result.append(item)
                continue

            query = self._qb.get_all_instances_of_class(class_name_camel)

            for solution in self._store.query(query): # type: ignore
                node = solution["s"]
                if node:
                    obj = self._uri_to_pydantic(node)
                    if obj:
                        item_id = getattr(obj, "id", None)
                        if item_id and item_id not in seen_ids:
                            result.append(obj)
                            seen_ids.add(item_id)
                        elif not item_id:
                            result.append(obj)

        # Apply taxonomy filter
        if taxonomy is not None:
            result = list(
                filter(
                    lambda instance: hasattr(instance, "isDefinedByTaxonomy")
                    and instance.isDefinedByTaxonomy in taxonomies,
                    result,
                )
            )

        # Apply vocabulary filter
        if vocabulary is not None:
            result = list(
                filter(
                    lambda instance: hasattr(instance, "isDefinedByVocabulary")
                    and instance.isDefinedByVocabulary == vocabulary,
                    result,
                )
            )

        # Apply document filter
        if document is not None:
            result = list(
                filter(
                    lambda instance: hasattr(instance, "hasDocumentation")
                    and instance.hasDocumentation == document,
                    result,
                )
            )

        if result is None:
            result = []

        self._combined_cache[cache_key] = result

        return result if isinstance(result, list) else [result]

    def get_by_id(self, class_name: Optional[str], identifier: str) -> Optional[Any]:
        """
        Get a single instance by its identifier.

        Args:
            class_name: str | None
                Name of the class
            identifier: str
                The id value of the instance

        Returns:
            Pydantic object or None
        """
        return self._id_cache.get(identifier)

    def get_by_attribute(
        self, class_name: str, attribute: str, value: Any
    ) -> List[Any]:
        """
        Get all instances that match a specific attribute value.

        Args:
            class_name: str
                Name of the class to filter
            attribute: str
                Attribute name to filter by
            value: Any
                Value to match

        Returns:
            list: List of matching Pydantic instances
        """
        class_name_camel = self._collection_map.get(class_name)
        if not class_name_camel:
            return []

        # Format the value for SPARQL
        if isinstance(value, bool):
            sparql_value = f'"{str(value)}"^^<http://www.w3.org/2001/XMLSchema#boolean>'
        elif isinstance(value, int):
            sparql_value = f'"{value}"^^<http://www.w3.org/2001/XMLSchema#integer>'
        elif isinstance(value, float):
            sparql_value = f'"{value}"^^<http://www.w3.org/2001/XMLSchema#decimal>'
        elif isinstance(value, str):
            escaped = value.replace('"', '\\"')
            sparql_value = f'"{escaped}"'
        else:
            sparql_value = f'"{str(value)}"'

        query = self._qb.get_instances_by_attribute(class_name_camel, attribute, sparql_value)

        result = []
        try:
            for solution in self._store.query(query):
                node = solution["s"]
                if node:
                    obj = self._uri_to_pydantic(node)
                    if obj:
                        result.append(obj)
        except Exception:
            pass

        return result

    def get_attribute(
        self, class_name: str, identifier: str, attribute: str
    ) -> Optional[Any]:
        """
        Get a specific attribute value from an instance.

        Args:
            class_name: str
                Name of the class (unused but kept for API compatibility)
            identifier: str
                Identifier of the instance
            attribute: str
                Attribute name to retrieve

        Returns:
            Any: The attribute value or None
        """
        instance = self.get_by_id(class_name, identifier)
        if instance and hasattr(instance, attribute):
            return getattr(instance, attribute)
        return None

    def query(self, class_name: str, **kwargs) -> List[Any]:
        """
        Query instances by class and attribute filters.

        Args:
            class_name: str
                Name of the class to query
            **kwargs: Attribute-value pairs to filter by

        Returns:
            list: List of matching Pydantic instances
        """
        if not kwargs:
            return self.get_all(class_name)

        return self.filter_instances(class_name, kwargs)

    def filter_instances(self, class_name: str, filters: Dict[str, Any]) -> List[Any]:
        """
        Filter instances by multiple criteria (AND logic).

        Args:
            class_name: str
                Name of the class to filter
            filters: dict
                Dictionary of attribute-value pairs

        Returns:
            list: List of matching Pydantic instances
        """
        if not filters:
            return self.get_all(class_name)

        instances = self.get_all(class_name)
        matches = []

        for instance in instances:
            match = []
            for k, v in filters.items():
                if v is not None:
                    attr_val = getattr(instance, k, None)
                    if (
                        isinstance(attr_val, str) and attr_val == v
                    ) or (isinstance(attr_val, list) and v in attr_val):
                        match.append(1)
                    else:
                        match.append(0)

            if 0 not in match:
                matches.append(instance)

        return matches

    def filter_ids_by_type(
        self, ids: List[str], disallowed_types: List[str]
    ) -> List[str]:
        """
        Filter a list of IDs to remove ones of specified types.

        Args:
            ids: list[str]
                List of ids to filter
            disallowed_types: list[str]
                The types to disallow

        Returns:
            list[str]: Filtered list of ids
        """
        return [
            id_
            for id_ in ids
            if id_ in self._id_cache
            and type(self._id_cache[id_]).__name__ not in disallowed_types
        ]

    def arrange_ids_by_type(self, ids: List[str]) -> Dict[str, List[str]]:
        """
        Arrange a list of IDs organised by type.

        Args:
            ids: list[str]
                List of ids to arrange

        Returns:
            dict: IDs grouped by type
        """
        result = defaultdict(list)
        for id_ in ids:
            if id_ in self._id_cache:
                r_type = type(self._id_cache[id_]).__name__
                result[r_type].append(id_)

        return dict(result)

    def sparql_query(self, query_str: str) -> List[Dict[str, str]]:
        """
        Execute a raw SPARQL query against the store.

        Args:
            query_str: str
                SPARQL query string

        Returns:
            list[dict]: Query results as list of dicts
        """
        try:
            results = self._store.query(query_str)
            if isinstance(results, bool):
                return [{"result": str(results)}]

            output = []
            var_list = list(results.variables) if hasattr(results, "variables") else []

            for solution in results:
                row_dict = {}
                for var in var_list:
                    val = solution[var]
                    if val is not None:
                        if isinstance(val, pyoxigraph.NamedNode):
                            row_dict[str(var)] = str(val)
                        elif isinstance(val, pyoxigraph.Literal):
                            row_dict[str(var)] = val.value
                        else:
                            row_dict[str(var)] = str(val)
                    else:
                        row_dict[str(var)] = None
                output.append(row_dict)
            return output
        except Exception as e:
            return [{"error": str(e)}]

    def object_similarity(
        self,
        entry_a: Any,
        entry_b: Any,
        threshold: float,
        property_scores: Dict[str, Any],
        max_depth: int = 1,
        weight_dict: Dict[str, float] = {},
    ) -> float:
        """
        Measure how similar two objects are.

        Args:
            entry_a: Any
                Entry object instance
            entry_b: Any
                Entry object instance
            threshold: float
                The minimum score to consider nested objects as equivalent
            property_scores: dict
                Mutable dict to hold individual property scores, weights, contributing scores.
                Updated with keys per field + '_sum_of_weights' and '_final_score'.
            max_depth: int
                Recursion depth for comparing referenced objects (default 1)
            weight_dict: dict
                Override weights for fields; weight=0 skips the field (default equal weights)

        Returns:
            float: A number between 0.0 and 100.0 as a measurement of similarity.
        """
        if not hasattr(entry_a, "model_fields"):
            return 0.0

        total_weight = 0.0
        weighted_score = 0.0

        try:
            fields = entry_a.__class__.model_fields
        except (AttributeError, TypeError):
            fields = entry_a.model_fields

        for field_name in fields:
            weight = weight_dict.get(field_name, 1.0)
            if weight == 0:
                continue

            val_a = getattr(entry_a, field_name, None)
            val_b = getattr(entry_b, field_name, None)

            if val_a is None and val_b is None:
                continue

            score = self._compare_values(val_a, val_b, max_depth, threshold)

            property_scores[field_name] = {
                "score": score,
                "weight": weight,
                "contributing_score": score * weight,
            }

            total_weight += weight
            weighted_score += score * weight

        if total_weight == 0:
            return 0.0

        final_score = weighted_score / total_weight
        property_scores["_sum_of_weights"] = total_weight
        property_scores["_final_score"] = final_score

        return final_score

    def object_equivalence(
        self,
        entry_a: Any,
        entry_b: Any,
        threshold: float,
        property_scores: Dict[str, Any],
        max_depth: int = 1,
        weight_dict: Dict[str, float] = {},
    ) -> bool:
        """
        Measure semantic object equivalence based on similarity threshold.

        Args:
            entry_a: Any
                Entry object instance
            entry_b: Any
                Entry object instance
            threshold: float
                The minimum score to result in successfully calling both objects equivalent
            property_scores: dict
                Mutable dict to hold individual property scores (passed to object_similarity)
            max_depth: int
                Recursion depth for comparing referenced objects (default 1)
            weight_dict: dict
                Override weights for fields; weight=0 skips the field (default equal weights)

        Returns:
            bool: True if similarity >= threshold, False otherwise.
        """
        similarity = self.object_similarity(entry_a, entry_b, threshold, property_scores, max_depth, weight_dict)
        return similarity >= threshold

    def get_star_graph(self, entity_id: str, max_depth: int = 1) -> StarGraph:
        """
        Extract the multi-hop neighborhood (star graph) of an entity via BFS.

        Args:
            entity_id: str
                The ID of the entity to build a star graph around
            max_depth: int
                Maximum hop distance to traverse. Defaults to 1 for 1-hop neighborhood.

        Returns:
            StarGraph: A dataclass containing the center entity and its resolved neighbors
                       from all hops up to max_depth, merged by field name.

        Raises:
            ValueError: If the entity_id is not found in the id cache
        """
        center = self._id_cache.get(entity_id)
        if center is None:
            raise ValueError(f"Entity '{entity_id}' not found in id cache")

        NON_REFERENCE_FIELDS = {"id", "name", "description", "tag", "url",
                                "concern", "dateCreated", "dateModified"}
        all_neighbors: Dict[str, List[Any]] = defaultdict(list)
        seen_ids: Set[str] = {entity_id}
        frontier = [entity_id]

        for _ in range(max_depth):
            next_frontier = []
            for current_id in frontier:
                node = self._id_cache.get(current_id)
                if node is None:
                    continue
                for field_name in node.__class__.model_fields:
                    if field_name in NON_REFERENCE_FIELDS:
                        continue
                    value = getattr(node, field_name, None)
                    if value is None:
                        continue

                    if isinstance(value, str):
                        candidates = [value]
                    elif isinstance(value, list) and all(isinstance(v, str) for v in value):
                        candidates = value
                    else:
                        continue

                    for v in candidates:
                        if v in self._id_cache and v not in seen_ids:
                            all_neighbors[field_name].append(self._id_cache[v])
                            seen_ids.add(v)
                            next_frontier.append(v)
            frontier = next_frontier
            if not frontier:
                break

        return StarGraph(
            center_id=entity_id,
            center=center,
            neighbors={k: v for k, v in all_neighbors.items() if v},
        )

    def compare_star_graphs(self, id_a: str, id_b: str, max_depth: int = 1) -> StarGraphComparison:
        """
        Compare the star graphs of two entities.

        Args:
            id_a: str
                ID of the first entity
            id_b: str
                ID of the second entity
            max_depth: int
                Maximum hop distance to traverse. Defaults to 1 for 1-hop neighborhood.

        Returns:
            StarGraphComparison: A dataclass with Jaccard similarity, shared/unique neighbors,
                                and per-field breakdown
        """
        graph_a = self.get_star_graph(id_a, max_depth=max_depth)
        graph_b = self.get_star_graph(id_b, max_depth=max_depth)

        ids_a = graph_a.neighbor_ids
        ids_b = graph_b.neighbor_ids

        shared = ids_a & ids_b
        unique_a = ids_a - ids_b
        unique_b = ids_b - ids_a
        union = ids_a | ids_b
        jaccard = len(shared) / len(union) if union else 0.0

        # Per-field breakdown
        all_fields = set(graph_a.neighbors) | set(graph_b.neighbors)
        per_field: Dict[str, Dict[str, Any]] = {}
        for f in all_fields:
            a_ids = {o.id for o in graph_a.neighbors.get(f, []) if hasattr(o, "id")}
            b_ids = {o.id for o in graph_b.neighbors.get(f, []) if hasattr(o, "id")}
            per_field[f] = {
                "shared": a_ids & b_ids,
                "unique_to_a": a_ids - b_ids,
                "unique_to_b": b_ids - a_ids,
            }

        return StarGraphComparison(
            graph_a=graph_a,
            graph_b=graph_b,
            shared_neighbor_ids=shared,
            unique_to_a=unique_a,
            unique_to_b=unique_b,
            jaccard_similarity=round(jaccard, 4),
            per_field=per_field,
        )

    def clear_cache(self):
        """Manually clear caches."""
        self._combined_cache.clear()
        # Don't clear _id_cache as it's built from the Pydantic data, not the query cache
        # self._id_cache.clear()
