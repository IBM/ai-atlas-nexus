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

        if entity_id not in [d['id'] for d in total_instances]:
            total_instances.append(entity)
            instances_for_class.append(entity)
        else:
            combined_entity = [d for d in total_instances if d['id'] == entity_id][0]
            for key, value in entity.items():
                if key == "id":
                    pass
                elif key == "type":
                    if key not in combined_entity:
                        combined_entity[key] = value
                else:
                    if key not in combined_entity:
                        combined_entity[key] = value
                    else:
                        if combined_entity[key] is not None:
                            if type(combined_entity[key]) != list:
                                pass
                            else:
                                combined_entity[key] = list(set([
                                    *combined_entity[key],
                                    *value,
                                ]))
                        else:
                            combined_entity[key] = value

            total_instances = [combined_entity if d['id'] == entity_id else d for d in total_instances]

            if entity_id not in [d['id'] for d in instances_for_class]:
                instances_for_class = [combined_entity if d['id'] == entity_id else d for d in instances_for_class]
            else:
                instances_for_class.append(combined_entity)

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
    total_instances = []
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
