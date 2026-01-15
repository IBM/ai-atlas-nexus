from typing import Any, Dict, List

import inflect

from ai_atlas_nexus.blocks.risk_explorer.base import ExplorerBase
from ai_atlas_nexus.data.knowledge_graph import *


ie = inflect.engine()

class AtlasExplorer(ExplorerBase):

    def __init__(self, data):

        # load the data into the graph
        self._data = data

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
            instances = collection_data if isinstance(collection_data, list) else []

            for instance in instances:
                instance_type_name = type(instance).__name__
                possible_singular = ie.singular_noun(class_name)
                if instance_type_name.lower() == class_name or (possible_singular and instance_type_name.lower() == possible_singular.lower()):
                    result.append(instance)

        return result

    def get_all(self, class_name=None, taxonomy=None, vocabulary=None, document=None):
        """
        Get all the instances of a specified class.

        Args:
            class_name: Union[str | list | None]:
                Name of the class (the collection key in data)
            taxonomy: str
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

        if isinstance(class_name, str):
            class_names.append(class_name)
        else:
            class_names = class_name
        result = []

        for key in class_names:
            if key not in self._data:
                for k in self._data.model_fields_set:
                    # snake_case and the actual class name
                    if k.lower().replace('_', '') == key.lower().replace('_', ''):
                        key = k
                        break

            if hasattr(self._data, key):
                result = getattr(self._data, key)
            else:
                result = self._check_subclasses(result, class_name)

        if taxonomy is not None:
            result = list(
                filter(
                    lambda instance: instance.isDefinedByTaxonomy == taxonomy, result
                )
            )
        if vocabulary is not None:
            result = list(
                filter(
                    lambda instance: instance.isDefinedByVocabulary == vocabulary, result
                )
            )

        if document is not None:
            result = list(
                filter(
                    lambda instance: instance.hasDocumentation == document, result
                )
            )
        if result is None:
            result = []

        return result if isinstance(result, list) else [result]

    def get_by_id(self, class_name, identifier):
        """
        Get a single instance by its identifier.

        Args:
            class_name: str
                Name of the class (the collection key in data)
            identifier: str
                Value of the identifier field

        Returns:
            Optional[Dict[str, Any]]
                The matching instance or None
        """
        instances = self.get_all(class_name)

        # Hmm assuming here all entities have id perhaps should check as it is not enforced
        id_slot = 'id'

        for instance in instances:
            if getattr(instance,id_slot) == identifier:
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
            if (type(getattr(instance, attribute)) == str and getattr(instance, attribute) == value) or (type(getattr(instance, attribute)) == List and getattr(instance, attribute).contains(value)):
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
                    if ((type(getattr(instance, k)) == str and getattr(instance, k) == v) or (type(getattr(instance, k)) == list and v in getattr(instance, k))):
                        match.append(1)
                    else:
                        match.append(0)

            if not 0 in match:
                matches.append(instance)

        return matches
