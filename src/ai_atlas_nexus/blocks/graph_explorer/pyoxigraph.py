import logging
import re
from collections import defaultdict
from typing import Any, Dict, List, Optional, Set
from urllib.parse import quote, unquote

import inflect
import pyoxigraph
from pydantic import BaseModel

from ai_atlas_nexus.blocks.graph_explorer.base import ExplorerBase
from ai_atlas_nexus.blocks.graph_explorer.query_builder import (
    NEXUS_URI,
    SPARQLQueryBuilder,
)
from ai_atlas_nexus.blocks.prompt_builder import ZeroShotPromptBuilder
from ai_atlas_nexus.blocks.prompt_templates import NL_TO_SPARQL_TEMPLATE
from ai_atlas_nexus.data.knowledge_graph import *
from ai_atlas_nexus.exceptions import InvalidSPARQLQueryException


try:
    from txtai import Embeddings
except ImportError:
    Embeddings = None

ie = inflect.engine()
logger = logging.getLogger(__name__)


class PyoxigraphExplorer(ExplorerBase):

    def __init__(self, data):
        """
        Initialize Pyoxigraph Explorer by loading LinkML data into a pyoxigraph Store.

        Args:
            data: Container
                Container object, populated instance of the knowledge graph
        """
        self._data = data
        self._embeddings = None
        self._qb = SPARQLQueryBuilder()
        self._data_types = []
        self._store = self._load_data_to_store(data)

    def get_all_classes(self):
        """
        Get all the class names that have data in the knowledge graph.

        Returns:
             list[str]
        """
        results = []
        rs = self._store.query(self._qb.get_all_classes())
        classes = [str(row["class"]) for row in rs]

        for uri_str in classes:
            identifier = self._format_uri_str(uri_str)
            if identifier:
                results.append(identifier)

        return results

    def _check_subclasses(self, result, class_name):
        """
        Look for subclasses within container collections

        Args:
            result: list
                Append any subclasses to this result list
            class_name: str
                The name of class
        Returns:
            result: list
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

    def _load_data_to_store(self, data):
        """
        Load Container into a pyoxigraph Store by building RDF quads from Pydantic objects.

        Args:
            data: Container object, populated instance of the knowledge graph

        Returns:
            pyoxigraph.Store
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

                # URI-encode the ID for special characters
                encoded_id = quote(str(item_id), safe="")
                item_uri = pyoxigraph.NamedNode(f"{NEXUS_URI}{encoded_id}")

                if item_uri in seen_iris:
                    continue
                seen_iris.add(item_uri)

                # Add rdf:type quad
                class_name = type(item).__name__
                class_uri = pyoxigraph.NamedNode(f"{NEXUS_URI}{class_name}")
                rdf_type = pyoxigraph.NamedNode(
                    "http://www.w3.org/1999/02/22-rdf-syntax-ns#type"
                )
                store.add(pyoxigraph.Quad(item_uri, rdf_type, class_uri, None))

                # Add property quads
                for field_name_attr, field_value in item:
                    if field_value is None or field_name_attr.startswith("_"):
                        continue

                    prop_uri = pyoxigraph.NamedNode(
                        f"{NEXUS_URI}{field_name_attr}"
                    )

                    if isinstance(field_value, str):
                        obj = pyoxigraph.Literal(field_value)
                    elif isinstance(field_value, bool):
                        obj = pyoxigraph.Literal(
                            str(field_value).lower(),
                            datatype=pyoxigraph.NamedNode(
                                "http://www.w3.org/2001/XMLSchema#boolean"
                            ),
                        )
                    elif isinstance(field_value, int):
                        obj = pyoxigraph.Literal(
                            str(field_value),
                            datatype=pyoxigraph.NamedNode(
                                "http://www.w3.org/2001/XMLSchema#integer"
                            ),
                        )
                    elif isinstance(field_value, float):
                        obj = pyoxigraph.Literal(
                            str(field_value),
                            datatype=pyoxigraph.NamedNode(
                                "http://www.w3.org/2001/XMLSchema#decimal"
                            ),
                        )
                    elif isinstance(field_value, list):
                        # Add multiple quads for list values
                        for list_item in field_value:
                            if isinstance(list_item, str):
                                obj = pyoxigraph.Literal(list_item)
                                store.add(
                                    pyoxigraph.Quad(
                                        item_uri, prop_uri, obj, None
                                    )
                                )
                        continue
                    else:
                        obj = pyoxigraph.Literal(str(field_value))

                    store.add(pyoxigraph.Quad(item_uri, prop_uri, obj, None))

        return store

    def _uri_to_pydantic(self, node):
        """
        Convert a pyoxigraph NamedNode to a Pydantic object by scanning self._data.

        Args:
            node: pyoxigraph.NamedNode
                The node to convert

        Returns:
            Optional[Any]
        """

        uri_str = str(node)
        # NamedNode.__str__() includes angle brackets, e.g. "<http://...>"
        if uri_str.startswith("<") and uri_str.endswith(">"):
            uri_str = uri_str[1:-1]
        if uri_str.startswith(NEXUS_URI):
            encoded_id = uri_str[len(NEXUS_URI) :]
            identifier = unquote(encoded_id)

            # Scan self._data to find the item by id
            for field_name in self._data.model_fields_set:
                items = getattr(self._data, field_name) or []
                for item in items:
                    if hasattr(item, "id") and item.id == identifier:
                        return item
        return None

    def get_all(
        self,
        class_name: Optional[str] = None,
        taxonomy: Optional[str] = None,
        vocabulary: Optional[str] = None,
        document: Optional[str] = None,
    ):
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

        result = []
        seen_ids = set()

        for key in class_names:
            # Resolve collection key from model
            if key not in self._data.model_fields_set:
                for k in self._data.model_fields_set:
                    if k.lower().replace("_", "") == key.lower().replace(
                        "_", ""
                    ):
                        key = k
                        break

            # Derive class name from self._data
            items = getattr(self._data, key, None) or []
            class_name_camel = type(items[0]).__name__ if items else None

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

            query = self._qb.get_all_instances_of_class(
                class_name_camel, taxonomy, vocabulary, document
            )

            for solution in self._store.query(query):
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

        return result

    def get_by_id(self, class_name, identifier):
        """
        Get a single instance by its identifier.

        Args:
            class_name: str | None
                Name of the class (the collection key in data)
            identifier: str
                Value of the identifier field

        Returns:
            Optional[Dict[str, Any]]
                The matching instance or None
        """
        if len(identifier) < 1:
            raise ValueError(f"No identifier provided: {identifier}")

        try:
            # Query the store to resolve the identifier to a Pydantic object
            encoded_id = quote(str(identifier), safe="")
            item_uri = pyoxigraph.NamedNode(f"{NEXUS_URI}{encoded_id}")
            return self._uri_to_pydantic(item_uri)
        except InvalidSPARQLQueryException:
            raise
        except Exception as e:
            return [{"error": str(e)}]

    def get_by_attribute(self, class_name, attribute, value):
        """
        Get all the instances that match a specific attribute value.

        Args:
            class_name: str
                Name of the class (the collection key in data)
            attribute: str
                Attribute name to filter by
            value: Any
                Value to match

        Returns:
            List[Dict[str, Any]]
                List of matching instances
        """
        # Resolve collection key from model
        type_names = self._resolve_key(class_name)
        # Format value as SPARQL literal with proper type decoration
        sparql_value = self._to_sparql_literal(value)

        query = self._qb.get_instances_by_attribute(
            type_names, attribute, sparql_value
        )

        matches = []
        for solution in self._store.query(query):
            node = solution["s"]
            if node:
                obj = self._uri_to_pydantic(node)
                if obj:
                    matches.append(obj)

        return matches

    def get_attribute(self, class_name, identifier, attribute):
        """
        Get a specific attribute value from an instance by querying the store.

        Args:
            class_name: str
                Name of the class (unused; kept for API compatibility)
            identifier: str
                Identifier of the instance
            attribute: str
                Attribute name to retrieve

        Returns:
            Any
                The attribute value or None
        """
        encoded_id = quote(str(identifier), safe="")
        subject_uri = f"{NEXUS_URI}{encoded_id}"
        predicate_uri = f"{NEXUS_URI}{attribute}"
        query = self._qb.get_by_subject_and_predicate(
            subject_uri, predicate_uri
        )

        results = list(self._store.query(query))
        if results:
            val = results[0]["o"]
            if isinstance(val, pyoxigraph.Literal):
                return val.value
            else:
                return str(val)
        return None

    def query(self, class_name, **kwargs):
        """
        A query method using keyword arguments.

        Args:
            class_name: Union[str | list]
                Name of the class (the collection key in data)
            **kwargs:
                The attribute-value pairs to filter by

        Returns:
            list[Dict[str, Any]]
                List of matching instances
        """
        return self.filter_instances(class_name, kwargs)

    @staticmethod
    def _to_sparql_literal(value):
        """Convert a Python value to a SPARQL literal with proper type decoration."""
        if isinstance(value, bool):
            return f'"{"true" if value else "false"}"^^xsd:boolean'
        if isinstance(value, int):
            return f'"{value}"^^xsd:integer'
        if isinstance(value, float):
            return f'"{value}"^^xsd:decimal'
        return f'"{value}"'

    def filter_instances(self, class_name, filters):
        """
        Filter instances by multiple criteria using a compound SPARQL query.

        Args:
            class_name: Union[str | list]
                Name of the class (the collection key in data)
            filters: Dict[str, Any]
                Dictionary of attribute-value pairs

        Returns:
            List[Dict[str, Any]]
                List of matching instances
        """
        # Resolve collection key from model (mirrors get_all() logic)
        class_name_camel = self._resolve_key(class_name)

        # Build SPARQL filters for non-None values
        sparql_filters = {}
        for k, v in filters.items():
            if v is not None:
                sparql_filters[k] = self._to_sparql_literal(v)

        # Query the store with all filters ANDed together
        query = self._qb.get_instances_by_attributes(
            class_name_camel, sparql_filters
        )

        matches = []
        for solution in self._store.query(query):
            node = solution["s"]
            if node:
                obj = self._uri_to_pydantic(node)
                if obj:
                    matches.append(obj)

        return matches

    def filter_ids_by_type(self, ids, disallowed_types):
        """
        Filter a list of IDs to remove ones of type

        Args:
            ids: List[str]
                List of ids to filter
            disallowed_types: List[str]
                The types to exclude

        Returns:
            List[str]

        """
        if not ids:
            return []

        ids = [item.id if hasattr(item, "id") else item for item in ids]

        # Build URIs for all IDs and query their types in a single SPARQL query
        subject_uris = [
            f"{NEXUS_URI}{quote(str(id_), safe='')}" for id_ in ids
        ]
        query = self._qb.get_types_for_subjects(subject_uris)

        result = []
        id_to_type = {}
        for solution in self._store.query(query):
            subject_uri = str(solution["s"])
            type_uri = str(solution["type"])

            # Strip angle brackets and NEXUS_URI prefix to get the type name
            if subject_uri.startswith("<") and subject_uri.endswith(">"):
                subject_uri = subject_uri[1:-1]
            if type_uri.startswith("<") and type_uri.endswith(">"):
                type_uri = type_uri[1:-1]

            if subject_uri.startswith(NEXUS_URI) and type_uri.startswith(
                NEXUS_URI
            ):
                identifier = unquote(subject_uri[len(NEXUS_URI) :])
                type_name = unquote(type_uri[len(NEXUS_URI) :])
                id_to_type[identifier] = type_name

        # Return IDs whose types are not in disallowed list
        for id_ in ids:
            if id_to_type.get(id_) not in disallowed_types:
                result.append(id_)

        return result

    def arrange_ids_by_type(self, ids):
        """
        Arrange a list of IDs to organise by type

        Args:
            ids: List[str]
                List of ids to organize

        Returns:
            dict

        """
        if not ids:
            return defaultdict(list)

        ids = [item.id if hasattr(item, "id") else item for item in ids]

        # Build URIs for all IDs and query their types in a single SPARQL query
        subject_uris = [
            f"{NEXUS_URI}{quote(str(id_), safe='')}" for id_ in ids
        ]
        query = self._qb.get_types_for_subjects(subject_uris)

        result = defaultdict(list)
        for solution in self._store.query(query):
            subject_uri = str(solution["s"])
            type_uri = str(solution["type"])

            # Strip angle brackets and NEXUS_URI prefix
            if subject_uri.startswith("<") and subject_uri.endswith(">"):
                subject_uri = subject_uri[1:-1]
            if type_uri.startswith("<") and type_uri.endswith(">"):
                type_uri = type_uri[1:-1]

            if subject_uri.startswith(NEXUS_URI) and type_uri.startswith(
                NEXUS_URI
            ):
                identifier = unquote(subject_uri[len(NEXUS_URI) :])
                type_name = unquote(type_uri[len(NEXUS_URI) :])
                result[type_name].append(identifier)

        return result

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
            try:
                results = self._store.query(query_str)
            except SyntaxError as e:
                raise InvalidSPARQLQueryException(str(e))

            if isinstance(results, bool):
                return [{"result": str(results)}]

            output = []
            var_list = (
                list(results.variables)
                if hasattr(results, "variables")
                else []
            )

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
        except InvalidSPARQLQueryException:
            raise
        except Exception as e:
            return [{"error": str(e)}]

    @staticmethod
    def _get_result_type(term) -> str:
        if isinstance(term, pyoxigraph.Literal):
            return "literal"
        elif isinstance(term, pyoxigraph.NamedNode):
            return "uri"
        elif isinstance(term, pyoxigraph.BlankNode):
            return "bnode"
        else:
            raise ValueError(f"Unknown type: {type(term)}")

    def _format_uri_str(self, uri_str):
        if uri_str.startswith("<") and uri_str.endswith(">"):
            uri_str = uri_str[1:-1]
        if uri_str.startswith(NEXUS_URI):
            encoded_id = uri_str[len(NEXUS_URI) :]
            identifier = unquote(encoded_id)
            return identifier

    def _resolve_key(self, class_name):
        key = class_name
        if key not in self._data.model_fields_set:
            for k in self._data.model_fields_set:
                if k.lower().replace("_", "") == key.lower().replace("_", ""):
                    key = k
                    break

        items = getattr(self._data, key, None) or []
        type_names = list(
            {type(i).__name__ for i in items if isinstance(i, BaseModel)}
        )
        if type_names and len(type_names) > 0:
            return type_names
        else:
            class_name_camel = None
            # Fallback: scan all collections for matching type name
            possible_singular = ie.singular_noun(class_name) or class_name
            for _, collection_data in self._data:
                instances = (
                    collection_data
                    if isinstance(collection_data, list)
                    else []
                )
                for instance in instances:
                    iname = type(instance).__name__
                    if iname.lower() in (
                        class_name.lower(),
                        possible_singular.lower(),
                    ):
                        class_name_camel = iname
                        break
                if class_name_camel:
                    break

            if not class_name_camel:
                return []

            return [class_name_camel]

    def natural_language_query(
        self,
        question: str,
        inference_engine,
    ) -> List[Dict[str, str]]:
        """
        Translate a natural language question to SPARQL and execute it on the store.

        Args:
            question: str
                Natural language question about the knowledge graph
            inference_engine: InferenceEngine
                Any configured inference engine (Ollama, RITS, WML, vLLM, HF)

        Returns:
            list[dict]: Query results in the same format as sparql_query().
                        Returns an empty list if the LLM or SPARQL execution fails.
        """
        classes = sorted(set(self.get_all_classes()))
        prompt = ZeroShotPromptBuilder(NL_TO_SPARQL_TEMPLATE).build(
            question=question,
            classes=", ".join(classes),
        )

        try:
            outputs = inference_engine.chat(
                messages=[[{"role": "user", "content": prompt}]]
            )
            raw = outputs[0].prediction
        except Exception as e:
            logger.warning("NL-to-SPARQL: inference engine failed: %s", e)
            return []

        # Strip markdown code fences if present
        raw = re.sub(
            r"```(?:sparql)?\s*", "", raw, flags=re.IGNORECASE
        ).strip()

        # Ensure standard prefixes are defined
        if "PREFIX" not in raw.upper():
            raw = SPARQLQueryBuilder.PREFIXES + raw

        results = self.sparql_query(raw)

        if results and "error" in results[0]:
            logger.warning(
                "NL-to-SPARQL: generated query failed.\nSPARQL:\n%s\nError: %s",
                raw,
                results[0]["error"],
            )
            return []

        return results

    def _to_nquads(self) -> bytes:
        """Serialise the internal pyoxigraph Store to N-Quads bytes.

        Used by SHACLEngine to pass the data graph to pyshacl without
        introducing an rdflib dependency in the caller.
        """
        import io as _io

        buf = _io.BytesIO()
        self._store.dump(buf, format=pyoxigraph.RdfFormat.N_QUADS)
        return buf.getvalue()
