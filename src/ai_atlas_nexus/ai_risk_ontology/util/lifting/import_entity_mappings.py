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
from sssom.constants import (
    NO_TERM_FOUND,
    OBJECT_ID,
    PREDICATE_ID,
    PREDICATE_INVERT_DICTIONARY,
    PREDICATE_MODIFIER,
    PREDICATE_MODIFIER_NOT,
    SUBJECT_ID,
)
from sssom.parsers import parse_sssom_table
from sssom.util import invert_mappings

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

def inverse_predicates():
    """
    Map each predicate to its inverse: the SKOS and OWL inverses sssom-py knows,
    and the inverse that a slot of the schema declares.
    """
    declared = {
        view.get_uri(slot_name, expand=False): view.get_uri(slot.inverse, expand=False)
        for slot_name, slot in view.all_slots().items()
        if slot.inverse
    }
    return {**declared, **PREDICATE_INVERT_DICTIONARY}


INVERSE_PREDICATES = inverse_predicates()


def process_mapping_from_tsv_to_entity_mapping(file_name):
    """
    TSV to entity mappings from the file, each paired with its inverse.
    sssom-py inverts a mapping by swapping subject and object and replacing the
    predicate with its inverse, so A skos:broadMatch B becomes B skos:narrowMatch A.
    A mapping whose predicate has no inverse is paired with None.
    Note this doesn't check validity of the mapping
    """
    tsv_file_name = join(MAP_DIR, file_name)
    df = parse_sssom_table(file_path=tsv_file_name).df
    # A negated mapping, or one to sssom:NoTermFound, records that there is no
    # match, so it adds nothing to the graph.
    keep = (df[SUBJECT_ID] != NO_TERM_FOUND) & (df[OBJECT_ID] != NO_TERM_FOUND)
    if PREDICATE_MODIFIER in df.columns:
        keep &= df[PREDICATE_MODIFIER] != PREDICATE_MODIFIER_NOT
    triples = df.loc[keep, [SUBJECT_ID, PREDICATE_ID, OBJECT_ID]]

    # Each distinct triple is inverted once, so a repeated row gets its inverse too.
    invertible = triples[triples[PREDICATE_ID].isin(INVERSE_PREDICATES)].drop_duplicates()
    inverted = invert_mappings(
        invertible,
        merge_inverted=False,
        predicate_invert_dictionary=INVERSE_PREDICATES,
    )
    inverse_of = {
        tuple(invertible.loc[i]): EntityMap(row[SUBJECT_ID], row[OBJECT_ID], row[PREDICATE_ID])
        for i, row in inverted.iterrows()
    }
    return [
        (EntityMap(s, o, p), inverse_of.get((s, p, o)))
        for s, p, o in triples.itertuples(index=False, name=None)
    ]

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
        entity_maps: pairs of an entity map and its inverse, or None if it has none
    Returns:
        list
    """
    output_entities = []
    invalid_relationships = []

    for em, inverse in entity_maps:

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

            inverse_slot = find_slot_by_curie(inverse.relationship) if inverse else None
            if inverse_slot:
                object.__setattr__(new_instance_entity_inverse, inverse_slot[1], [inverse.target_entity_id])
            elif inverse:
                logger.info("No slot for inverse predicate_id: %s", inverse.relationship)
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
