import json
import random
import uuid
from datetime import date, datetime
from typing import Any, Dict, Union

from linkml_runtime import SchemaView
from linkml_runtime.dumpers.dumper_root import Dumper
from linkml_runtime.utils.context_utils import CONTEXTS_PARAM_TYPE
from linkml_runtime.utils.yamlutils import YAMLRoot
from pydantic import BaseModel

from ai_atlas_nexus.ai_risk_ontology.datamodel.ai_risk_ontology import Container


class JSONGraphDumper(Dumper):

    def __init__(self, schema_path):
        super().__init__()
        self.schema_view = SchemaView(schema_path)
        self.nodes = []
        self.edges = []

        self.clusters = []
        self.processed_ids = set()
        self.processed_tags = set()
        self.processed_clusters = set()


    def _export_schema_structure(self):
        """Export schema classes and slots as nodes, with relationships as edges."""

        # Export classes as nodes
        for class_name in self.schema_view.all_classes():
            cls = self.schema_view.get_class(class_name)

            if "type" in cls.model_fields_set:
                # check for a subclass
                label = cls.__getattribute__("type")
            else:
                label = cls.name

            if class_name not in self.processed_ids:
                class_node = {
                    "key": f"{class_name}",
                    "node_type": "schema_class",
                    "tag": "schema_class",
                    "name": label,
                    "label": label,
                    "description": cls.description or "",
                    "abstract": cls.abstract or False,
                    "attributes": {
                        "class_uri": cls.class_uri,
                        "definition_uri": cls.definition_uri,
                    },
                }
                self.nodes.append(class_node)
                self.processed_ids.add(class_node["key"])
                self.processed_tags.add("schema_class")

        # Export slots as nodes
        for slot_name in self.schema_view.all_slots():
            if slot_name not in self.processed_ids:
                slot = self.schema_view.get_slot(slot_name)
                slot_node = {
                    "key": f"schema_slot:{slot_name}",
                    "node_type": "schema_slot",
                    "tag": "schema_slot",
                    "name": slot_name,
                    "label": slot.name,
                    "description": slot.description or "",
                    "attributes": {
                        "range": slot.range,
                        "multivalued": slot.multivalued or False,
                        "required": slot.required or False,
                        "slot_uri": slot.slot_uri,
                    },
                }
                self.nodes.append(slot_node)
                self.processed_ids.add(slot_node["key"])
                self.processed_tags.add("schema_slot")

        # Export schema relationships as edges
        self._export_schema_relationships()
        self.nodes = [
            i for n, i in enumerate(self.nodes) if i not in self.nodes[n + 1 :]
        ]
        self.edges = [
            i for n, i in enumerate(self.edges) if i not in self.edges[n + 1 :]
        ]

    def _export_schema_relationships(self):
        """Export relationships between schema elements."""

        for class_name in self.schema_view.all_classes():
            cls = self.schema_view.get_class(class_name)

            # Inheritance relationships (is_a)
            if cls.is_a:
                self.edges.append(
                    {
                        "key": f"{class_name}_is_a_{cls.is_a}",
                        "source": f"{class_name}",
                        "target": f"{cls.is_a}",
                        "edge_type": "is_a",
                        "label": "is a",
                    }
                )

            # Mixin relationships
            if cls.mixins:
                for mixin in cls.mixins:
                    self.edges.append(
                        {
                            "key": f"{class_name}_mixin_{mixin}",
                            "source": f"{class_name}",
                            "target": f"{mixin}",
                            "edge_type": "mixin",
                            "label": "uses mixin",
                        }
                    )

            # Class-slot relationships
            for slot_name in self.schema_view.class_slots(class_name):
                slot = self.schema_view.get_slot(slot_name)

                # Class has slot
                self.edges.append(
                    {
                        "key": f"{class_name}_has_slot_{slot_name}",
                        "source": f"{class_name}",
                        "target": f"schema_slot:{slot_name}",
                        "edge_type": "has_slot",
                        "label": f"has slot {slot_name}",
                    }
                )

                # Slot points to range (if it's another class)
                if slot.range and slot.range in self.schema_view.all_classes():
                    self.edges.append(
                        {
                            "key": f"{slot_name}_range_{slot.range}",
                            "source": f"schema_slot:{slot_name}",
                            "target": f"{slot.range}",
                            "edge_type": "has_range",
                            "label": f"range: {slot.range}",
                        }
                    )

    def _export_data_object(
        self, obj: Any, object_id: str = None, inferred_type: str = None
    ):
        """Export the data object and its relationships."""

        if isinstance(obj, Container):
            # LinkML object
            obj_type = obj.__class__.__name__
            obj_dict = obj.__dict__
            obj_id = object_id or getattr(obj, "id", None) or str(uuid.uuid4())
            obj_cluster = "unknown"
        elif isinstance(obj, dict):
            # Dictionary object

            for key, value in obj.items():
                if value is not None:
                    obj_type = key

                    if isinstance(value, (dict, list)):
                        if isinstance(value, (list)):
                            obj_type = (
                                type(value[0]).__name__
                                if (value is not None and len(value) > 0)
                                else inferred_type
                            )
                        else:
                            print(value, type(value))
                            obj_type = (
                                type(value)
                                if value is not None
                                else inferred_type
                            )

                        for item in value:
                            obj_cluster = (
                                item.isDefinedByTaxonomy
                                if hasattr(item, "isDefinedByTaxonomy")
                                else "unknown"
                            )
                            # Create data instance node
                            data_node_id = f"{item.id}"
                            if data_node_id not in self.processed_ids:
                                data_node = {
                                    "key": data_node_id,
                                    "node_type": "data_instance",
                                    "name": item.name,
                                    "description": item.description or "",
                                    "label": f"{data_node_id}",
                                    "tag": type(item).__name__ or "",
                                    "cluster": obj_cluster,
                                    "attributes": {},
                                }
                            obj_dict = item.dict()
                            # Add simple attributes (non-relational data)
                            for key, value in obj_dict.items():
                                if (
                                    not isinstance(value, (dict, list))
                                    and not key.startswith("_")
                                    and not isinstance(value, (date, datetime))
                                ):
                                    data_node["attributes"][key] = value

                            self.nodes.append(data_node)
                            self.processed_ids.add(data_node_id)
                            self.processed_tags.add(type(item).__name__ or "")
                            self.clusters.append(obj_cluster)
                            self.processed_clusters.add(obj_cluster)

                            # Connect to schema class if it exists
                            schema_class_id = f"{obj_type}"
                            if any(
                                n["key"] == schema_class_id for n in self.nodes
                            ):
                                self.edges.append(
                                    {
                                        "key": f"{obj_id}_instance_of_{obj_type}",
                                        "source": data_node_id,
                                        "target": schema_class_id,
                                        "edge_type": "instance_of",
                                        "label": "instance of",
                                    }
                                )

                            # Export relationships from this object
                            self._export_data_relationships(
                                obj_dict, data_node_id, obj_type
                            )
        else:
            return

    def _export_data_relationships(
        self, obj_dict: Dict, source_id: str, source_type: str
    ):
        """Export relationships from a data object."""

        for slot_name, value in obj_dict.items():
            if slot_name.startswith("_"):
                continue

            # Get slot information from schema if available
            slot_info = None
            try:
                if source_type in self.schema_view.all_classes():
                    class_slots = self.schema_view.class_slots(source_type)
                    if slot_name in class_slots:
                        slot_info = self.schema_view.get_slot(slot_name)
            except:
                pass

            if isinstance(value, list):
                # Handle multivalued relationships
                for i, item in enumerate(value):
                    if isinstance(item, dict):
                        target_id = item.get("id", f"{slot_name}_{i}")
                        target_node_id = f"{target_id}"

                        # Recursively export the related object
                        target_type = item.get(
                            "type",
                            slot_info.range if slot_info else "UnknownType",
                        )
                        self._export_data_object(
                            item,
                            object_id=target_id,
                            inferred_type=target_type,
                        )

                        # Create relationship edge
                        self.edges.append(
                            {
                                "key": f"{source_id}_{slot_name}_{target_id}",
                                "source": source_id,
                                "target": target_node_id,
                                "edge_type": "data_relationship",
                                "label": slot_name,
                                "slot_name": slot_name,
                            }
                        )
                    elif (
                        isinstance(item, str)
                        and slot_info
                        and slot_info.range in self.schema_view.all_classes()
                    ):
                        # String reference to another object
                        target_node_id = f"{item}"
                        self.edges.append(
                            {
                                "key": f"{source_id}_{slot_name}_{item}",
                                "source": source_id,
                                "target": target_node_id,
                                "edge_type": "data_reference",
                                "label": slot_name,
                                "slot_name": slot_name,
                            }
                        )

            elif isinstance(value, dict):
                # Single object relationship
                target_id = value.get("id", f"{slot_name}_obj")
                target_node_id = f"{target_id}"

                # Recursively export the related object
                target_type = value.get(
                    "type", slot_info.range if slot_info else "UnknownType"
                )
                self._export_data_object(
                    value, object_id=target_id, inferred_type=target_type
                )

                # Create relationship edge
                self.edges.append(
                    {
                        "key": f"{source_id}_{slot_name}_{target_id}",
                        "source": source_id,
                        "target": target_node_id,
                        "edge_type": "data_relationship",
                        "label": slot_name,
                        "slot_name": slot_name,
                    }
                )

            elif (
                isinstance(value, str)
                and slot_info
                and slot_info.range in self.schema_view.all_classes()
            ):
                # String reference to another object
                target_node_id = f"{value}"
                self.edges.append(
                    {
                        "key": f"{source_id}_{slot_name}_{value}",
                        "source": source_id,
                        "target": target_node_id,
                        "edge_type": "data_reference",
                        "label": slot_name,
                        "slot_name": slot_name,
                    }
                )

    def dump(
        self,
        element: Union[BaseModel, YAMLRoot],
        to_file: str,
        contexts: CONTEXTS_PARAM_TYPE = None,
        **kwargs,
    ) -> None:
        """
        Write element as json to to_file

        Args:
            element: Union[BaseModel, YAMLRoot]
                LinkML object to be output
            to_file: str
                file to write to
            contexts: Optional[Union[CONTEXT_TYPE, List[CONTEXT_TYPE]]]
                 a list of JSON-LD contexts, which can be one of:
                    * the name of a JSON-LD file
                    * the URI of a JSON-lD file
                    * JSON-LD text
                    * A JsonObj object that contains JSON-LD
                    * A dictionary that contains JSON-LD
        """
        if isinstance(element, BaseModel):
            element = element.dict()

        super().dump(element, to_file, contexts=contexts, **kwargs)

    def dumps(self, element: Union[BaseModel, YAMLRoot], **_) -> str:
        """
        Return element as json string with nodes, edges

        Args:
            element: Union[BaseModel, YAMLRoot],
                LinkML object to be emitted
            _:
                method specific arguments

        Returns:
            str
        """

        # First, export schema structure ( not including this at present)
        # self._export_schema_structure()

        # Then, export the data instances if provided
        self._export_data_object(element.__dict__)


        def _tag_output_format(tag):
            if tag == None or tag == "unknown":
                return {"key": "unknown", "image": "unknown.svg"}
            if tag == "Stakeholder":
                return {"key": "Stakeholder", "image": "person.svg"}
            if tag == "StakeholderGroup":
                return {"key": "StakeholderGroup", "image": "StakeholderGroup.svg"}
            if tag == "Action":
                return {"key": "Action", "image": "Action.svg"}
            if tag == "Organization":
                return {"key": "Organization", "image": "Organization.svg"}
            if tag == "Documentation":
                return {"key": "Documentation", "image": "Documentation.svg"}
            if tag == "Risk":
                return {"key": "Risk", "image": "Risk.svg"}
            if tag == "RiskIncident":
                return {"key": "RiskIncident", "image": "RiskIncident.svg"}
            if tag == "RiskGroup":
                return {"key": "RiskGroup", "image": "RiskGroup.svg"}
            if tag == "RiskTaxonomy":
                return {"key": "RiskTaxonomy", "image": "RiskTaxonomy.svg"}
            if tag == "Dataset":
                return {"key": "Dataset", "image": "Dataset.svg"}
            if tag == "License":
                return {"key": "License", "image": "License.svg"}
            if tag == "Principle":
                return {"key": "Principle", "image": "Principle.svg"}
            if tag == "Adapter":
                return {"key": "Adapter", "image": "Adapter.svg"}
            if tag == "LargeLanguageModel":
                return {"key": "LargeLanguageModel", "image": "LargeLanguageModel.svg"}
            else:
                return {"key": tag, "image": "unknown.svg"}

        self.edges = [
            i for n, i in enumerate(self.edges) if i not in self.edges[:n]
        ]

        def get_color_array(length):
            colors = []
            i = 0
            while True:
                r = random.randint(0, 255)
                g = random.randint(0, 255)
                b = random.randint(0, 255)
                colors.append(f"#{r:02x}{g:02x}{b:02x}")
                i += 1
                if i > length:
                    break
            return colors

        color_arr = get_color_array(len(self.processed_clusters))

        output = {
            "nodes": self.nodes,
            "edges": self.edges,
            "clusters": [
                {"key": cluster, "color": color_arr[index], "clusterLabel": cluster}
                for index, cluster in enumerate(self.processed_clusters)
            ],
            "tags": [_tag_output_format(tag) for tag in self.processed_tags],
            "metadata": {
                "schema_classes": len(
                    [
                        n
                        for n in self.nodes
                        if n.get("node_type") == "schema_class"
                    ]
                ),
                "schema_slots": len(
                    [
                        n
                        for n in self.nodes
                        if n.get("node_type") == "schema_slot"
                    ]
                ),
                "data_instances": len(
                    [
                        n
                        for n in self.nodes
                        if n.get("node_type") == "data_instance"
                    ]
                ),
                "total_nodes": len(self.nodes),
                "total_edges": len(self.edges),
            },
        }

        return json.dumps(output)
