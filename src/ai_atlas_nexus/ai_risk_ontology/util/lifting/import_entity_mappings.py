"""
Import entity mappings from the different TSV files.
Run this when you have are adding new TSV files.
There is an assumption some content already exists in graph
"""

# Standard Library
from os import listdir
from os.path import isfile, join
from pathlib import Path
from typing import Any, Type

# Third Party
from linkml_runtime.dumpers import YAMLDumper
from pydantic import BaseModel
from sssom.parsers import parse_sssom_table

from ai_atlas_nexus import AIAtlasNexus

# Local
from ai_atlas_nexus.ai_risk_ontology import Container
from ai_atlas_nexus.toolkit.logging import configure_logger


MAP_DIR = "src/ai_atlas_nexus/data/mappings/"
DATA_DIR = "src/ai_atlas_nexus/data/knowledge_graph/mappings/"

logger = configure_logger(__name__)

aan = AIAtlasNexus() # default config
view = aan.get_schema()

class EntityMap(BaseModel):
    src_entity_id: str
    target_entity_id: str
    relationship: str

    def __init__(self, src_entity_id: str, target_entity_id: str, relationship: str):
        src_id = src_entity_id.split(":")[-1]
        target_id = target_entity_id.split(":")[-1]

        super().__init__(
            src_entity_id=src_id,
            target_entity_id=target_id,
            relationship=relationship,
        )

def process_mapping_from_tsv_to_entity_mapping(file_name):
    """
    TSV to entity mapping from the file
    Note this doesn't check validity of the mapping
    """
    tsv_file_name = join(MAP_DIR, file_name)
    mapping_set_df = parse_sssom_table(file_path=tsv_file_name)
    ms = mapping_set_df.to_mapping_set()
    entity_maps = [
        EntityMap(
            **{
                "src_entity_id": item["subject_id"],
                "target_entity_id": item["object_id"],
                "relationship": item["predicate_id"],
            }
        )
        for item in ms.mappings
        if item["predicate_id"] != "noMatch"
    ]
    return entity_maps

def find_by_id(identifier):
    """
    Search for any object with matching id in the container
    it will check all collections in the container
     """
    fields = Container.model_fields
    for attr_name in fields:
        attr = getattr(aan._ontology, attr_name) or None
        if isinstance(attr, list):
            for item in attr:
                if hasattr(item, 'id') and item.id == identifier:

                    return (item, type(item))
    return None

def create_instance_from_class(item_class: Type, **kwargs) -> Any:
    return item_class(**kwargs)

def find_slot_by_curie(curie):
    for slot_name, slot in view.all_slots().items():
        slot_uri = view.get_uri(slot_name, expand=False)
        if slot_uri == curie:
            return (slot, slot_name)


def process_mappings_to_entities(entity_maps):
    """
    Processing an entity map into the linkml class output and include the inverse of the relationships.
    Args:
        entity_maps
    Returns:
        list
    """
    output_entities = []
    invalid_relationships = []

    for em in entity_maps:

        s_id = em.src_entity_id
        o_id = em.target_entity_id

        # determine the entities exist and their types
        entity, entity_class  = find_by_id(s_id)
        entity_for_inverse, entity_for_inverse_class = find_by_id(o_id)
        relationship = em.relationship

        new_instance_entity = create_instance_from_class(
            entity_class,
            id=s_id,
        )
        new_instance_entity_inverse = create_instance_from_class(
            entity_for_inverse_class,
            id=o_id,
        )

        # mapping logic
        # attempt to find relationships and we wnat their inverse
        try:
            slot, slot_name = find_slot_by_curie(relationship)
            object.__setattr__(new_instance_entity, slot_name, [o_id])

            if relationship in ["skos:closeMatch", "skos:exactMatch", "skos:broadMatch", "skos:narrowMatch", "skos:relatedMatch"]:
                object.__setattr__(new_instance_entity_inverse, slot_name, [s_id])
            elif hasattr(slot, "inverse") and slot.inverse is not None:
                object.__setattr__(new_instance_entity_inverse, slot.inverse, [s_id])
        except:
            logger.info("Unparseable predicate_id: %s", relationship)
            invalid_relationships.append(relationship)

        output_entities.append(new_instance_entity)
        output_entities.append(new_instance_entity_inverse)

    return output_entities

def prepare_container(output_entities):
    """
    Processing a lsit of linkml class output to a container.
    TODO: impove the logic of chnecking different subbranches like entries for items
    Args:
        output_entities
    Returns:
        Container
    """
    fields = Container.model_fields
    c = Container()
    for attr_name in fields:
        attr = getattr(aan._ontology, attr_name) or None
        if isinstance(attr, list):
             object.__setattr__(c, attr_name, [x for x in output_entities if type(x).__name__ == view.get_slot(attr_name).range or (attr_name == 'entries' and type(x).__name__ in view.class_descendants(view.get_slot(attr_name).range) ) or (attr_name == 'rules' and type(x).__name__ in view.class_descendants(view.get_slot(attr_name).range) )
                                               ])
    return c


def write_to_file(output_entities, output_file):
    with open(output_file, "+tw", encoding="utf-8") as output_file:
        container = prepare_container(output_entities)
        print(YAMLDumper().dumps(container), file=output_file)
        output_file.close()


if __name__ == "__main__":
    logger.info(f"Processing mapping files in : %s", MAP_DIR)
    mapping_files = [
        file_name
        for file_name in listdir(MAP_DIR)
        if (file_name.endswith(".md") == False) and isfile(join(MAP_DIR, file_name))
    ]
    for file_name in mapping_files:
        output_file = DATA_DIR + Path(file_name).stem + "_from_tsv_data.yaml"
        rs = process_mapping_from_tsv_to_entity_mapping(file_name)
        logger.info(f"Processed file: %s, %s valid entries", file_name, len(rs))
        outputs = process_mappings_to_entities(rs)
        write_to_file(outputs, output_file)
