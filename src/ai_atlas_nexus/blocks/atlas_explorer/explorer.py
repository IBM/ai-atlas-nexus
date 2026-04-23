from collections import defaultdict
from typing import Any, Dict, List

import inflect

from ai_atlas_nexus.blocks.atlas_explorer.base import ExplorerBase
from ai_atlas_nexus.data.knowledge_graph import *


ie = inflect.engine()


class AtlasExplorer(ExplorerBase):

    def __init__(self, data):

        # load the data into the graph
        self._data = data
        self._combined_cache = {}
        self._id_cache = {}
        self._build_id_cache_index()

    def _build_id_cache_index(self):
        """
        A dict which is mapping ID to LinkML obj
        """
        for class_name in self._data.model_fields_set:
            items = getattr(self._data, class_name) or []
            for item in items:
                if hasattr(item, 'id') and item.id:
                    self._id_cache[item.id] = item

    def get_all_classes(self):
        """
        Get all the class names that have data in the knowledge graph.

        Returns:
             list[str]
        """
        return list(self._data.model_fields_set)

    def _check_subclasses(self, result, class_name):
        # look for subclasses within container collections
        for collection_key, collection_data in self._data:
            instances = (
                collection_data if isinstance(collection_data, list) else []
            )

            for instance in instances:
                instance_type_name = type(instance).__name__
                possible_singular = ie.singular_noun(class_name)
                if instance_type_name.lower() == class_name or (
                    possible_singular
                    and instance_type_name.lower() == possible_singular.lower()
                ):
                    result.append(instance)

        return result

    def get_all(
        self, class_name=None, taxonomy=None, vocabulary=None, document=None
    ):
        """
        Get all the instances of a specified class.

        Args:
            class_name: Union[str | list | None]:
                Name of the class (the collection key in data)
            taxonomy: Union[str | list | None]
                (Optional) The string id for a taxonomy
            vocabulary:
                (Optional) The string id for a vocabulary
            document:
                (Optional) The string id for a document

        Returns:
            list[Dict[str, Any]]
                List of instances
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

        cache_key = (tuple(class_names) if isinstance(class_names, list) else class_name, tuple(taxonomies), vocabulary, document)

        if cache_key in self._combined_cache:
            return self._combined_cache[cache_key]

        result = []
        seen_ids = set()

        for key in class_names:
            if key not in self._data:
                for k in self._data.model_fields_set:
                    # snake_case and the actual class name
                    if k.lower().replace("_", "") == key.lower().replace(
                        "_", ""
                    ):
                        key = k
                        break

            if hasattr(self._data, key):
                items = getattr(self._data, key) or []
                for item in items:
                    item_id = getattr(item, "id", None)
                    if item_id and item_id not in seen_ids:
                        result.append(item)
                        seen_ids.add(item_id)
                    elif not item_id:
                        result.append(item)
            else:
                items = self._check_subclasses([], class_name)
                for item in items:
                    item_id = getattr(item, "id", None)
                    if item_id and item_id not in seen_ids:
                        result.append(item)
                        seen_ids.add(item_id)
                    elif not item_id:
                        result.append(item)

        if taxonomy is not None:
            result = list(
                filter(
                    lambda instance: hasattr(instance, "isDefinedByTaxonomy")
                    and instance.isDefinedByTaxonomy in taxonomies,
                    result,
                )
            )
        if vocabulary is not None:
            result = list(
                filter(
                    lambda instance: hasattr(instance, "isDefinedByVocabulary")
                    and instance.isDefinedByVocabulary == vocabulary,
                    result,
                )
            )

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
        if identifier in self._id_cache:
            return self._id_cache[identifier]

        if class_name:
            instances = self.get_all(class_name)

            # Hmm assuming here all entities have id perhaps should check as it is not enforced
            id_slot = "id"

            for instance in instances:
                if getattr(instance, id_slot) == identifier:
                    return instance

        return None

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
        instances = self.get_all(class_name)
        matches = []

        for instance in instances:
            if (
                type(getattr(instance, attribute)) == str
                and getattr(instance, attribute) == value
            ) or (
                type(getattr(instance, attribute)) == List
                and getattr(instance, attribute).contains(value)
            ):
                matches.append(instance)

        return matches

    def get_attribute(self, class_name, identifier, attribute):
        """
        Get a specific attribute value from an instance.

        Args:
            class_name: str
                Name of the class
            identifier: str
                Identifier of the instance
            attribute: str
                Attribute name to retrieve

        Returns:
            Any
                The attribute value or None
        """
        instance = self.get_by_id(class_name, identifier)
        if instance and isinstance(instance, dict):
            return instance.get(attribute)
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

    def filter_instances(self, class_name, filters):
        """
        Filter instances by multiple criteria.

        Args:
            class_name: Union[str | list]
                Name of the class (the collection key in data)
            filters: Dict[str, Any]
                Dictionary of attribute-value pairs

        Returns:
            List[Dict[str, Any]]
                List of matching instances
        """
        instances = self.get_all(class_name)
        matches = []

        for instance in instances:
            match = []
            for k, v in filters.items():
                if v is not None:
                    if (
                        type(getattr(instance, k)) == str
                        and getattr(instance, k) == v
                    ) or (
                        type(getattr(instance, k)) == list
                        and v in getattr(instance, k)
                    ):
                        match.append(1)
                    else:
                        match.append(0)

            if not 0 in match:
                matches.append(instance)

        return matches

    def filter_ids_by_type(self, ids, disallowed_types):
        """
        Filter a list of IDs to remove ones of type

        Args:
            ids: List[str]
                List of ids to filter
            allowed_types: List[str]
                The types to allow

        Returns:
            List[str]

        """
        return [
            id_ for id_ in ids
            if id_ in self._id_cache and type(self._id_cache[id_]).__name__ not in disallowed_types
        ]

    def arrange_ids_by_type(self, ids):
        """
        Arrange a list of IDs to organise by type

        Args:
            ids: List[str]
                List of ids to filter

        Returns:
            dict

        """
        result = defaultdict(list)
        for id_ in ids:
            if id_ in self._id_cache:
                r_type = type(self._id_cache[id_]).__name__
                if result.get(r_type):
                    result[r_type].append(id_)
                else:
                    result[r_type] =  [id_]

        return result

    def clear_cache(self):
          """
          Manually clear combined cache only.
          Don't need to clear _id_cache as it's built from the Pydantic data, not the query cache
          """
          self._combined_cache.clear()
