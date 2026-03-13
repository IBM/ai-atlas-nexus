import glob
import os

from linkml_runtime.loaders import yaml_loader

from ai_atlas_nexus.ai_risk_ontology.datamodel.ai_risk_ontology import Container
from ai_atlas_nexus.data import get_data_path
from ai_atlas_nexus.toolkit.logging import configure_logger


logger = configure_logger(__name__)

def combine_entities(total_instances, entities):
    """
    Combine entities with the same ID by merging their attributes.
    Some instance could be appearing under different keys
    """

    instances_for_class = []

    for entity in entities:
        entity_id = entity["id"]

        if entity_id not in total_instances:
            total_instances[entity_id] = entity
            instances_for_class.append(entity)
        else:
            combined_entity = total_instances[entity_id]
            for key, value in entity.items():
                if key == "id":
                    continue
                elif key not in combined_entity:
                    combined_entity[key] = value

                elif isinstance(combined_entity[key], list) and combined_entity[key]:
                    seen = set(combined_entity[key])
                    for item in value:
                          if item not in seen:
                              combined_entity[key].append(item)
                              seen.add(item)
                else:
                    combined_entity[key] = value

            total_instances[entity_id] = combined_entity

    return total_instances, instances_for_class


def load_yamls_to_container(base_dir):
    """Function to load the AIAtlasNexus with data

    Args:
        base_dir: str
            (Optional) user defined base directory path

    Returns:
        YAMLRoot instance of the Container class
    """

    # Get system yaml data path
    system_data_path = get_data_path()

    master_yaml_files = []
    for yaml_dir in [system_data_path, base_dir]:
        # Include YAML files from the user defined `base_dir` if exist.
        if yaml_dir is not None:
            master_yaml_files.extend(
                glob.glob(os.path.join(yaml_dir, "**", "*.yaml"), recursive=True)
            )

    yml_items_result = {}
    total_instances = {}
    for yaml_file in master_yaml_files:
        try:
            yml_items = yaml_loader.load_as_dict(source=yaml_file)
            for ontology_class, instances in yml_items.items():
                # Combine entries for entity types that may have mappings split across multiple files
                total_instances, instances_for_class = combine_entities(total_instances, instances)
                yml_items_result.setdefault(ontology_class, []).extend(instances_for_class)
        except Exception as e:
            logger.info(f"YAML ignored: {yaml_file}. Failed to load. {e}")


    ontology = yaml_loader.load_any(
        source=yml_items_result,
        target_class=Container,
    )

    return ontology
