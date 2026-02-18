"""
Base loader for loading data items from HuggingFace datasets to generic AI Atlas Nexus LinkML representation
"""

from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any, Dict, List, Optional

import yaml

from ai_atlas_nexus.toolkit.logging import configure_logger


logger = configure_logger(__name__)


class HFDataLoaderBase(ABC):
    """
    Abstract base class for loading HuggingFace dataset records into LinkML representations.

    For creating loaders that convert HuggingFace dataset
    records into LinkML-compatible data models and output them as YAML files.
    """

    def __init__(self, dataset_name, split = "train", subset = None):
        """
        Initialize the HuggingFace data loader.

        Args:
            dataset_name: str
                The HuggingFace dataset identifier (e.g., "ibm-research/Auto-BenchmarkCard")
            split: str
                The dataset split to use (default: "train")
            subset: Optional[str]
                subset/configuration name for the dataset
        """
        self.dataset_name = dataset_name
        self.split = split
        self.subset = subset
        self.dataset = None
        self._load_dataset()

    def _load_dataset(self):
        """Load the HuggingFace dataset."""
        try:
            from datasets import load_dataset

            if self.subset:
                self.dataset = load_dataset(self.dataset_name, self.subset, split=self.split)
            else:
                self.dataset = load_dataset(self.dataset_name, split=self.split)

            logger.info(f"Loaded dataset {self.dataset_name} with {len(self.dataset)} records")
        except ImportError:
            logger.error("datasets library not installed. Install with: pip install datasets")
            raise
        except Exception as e:
            logger.error(f"Failed to load dataset {self.dataset_name}: {e}")
            raise

    @abstractmethod
    def transform_record(self, record):
        """
        Transform a single HuggingFace dataset record into a LinkML representation.

        This method must be implemented by subclasses to define the transformation logic.

        Args:
            record:  Dict[str, Any]
                A single record from the HuggingFace dataset

        Returns:
            Dict[str, Any]
                A dictionary representing a LinkML entity
        """
        pass

    @abstractmethod
    def get_container_class_name(self):
        """
        Get the name of the LinkML container class to use.

        For example: "Container" or a domain-specific container class.

        Returns:
            str
                The LinkML container class name
        """
        pass

    def load_and_transform(self):
        """
        Load all the records from the dataset and transform them.

        Returns:
            List[Dict[str, Any]]
                A list of transformed LinkML entities
        """
        if not self.dataset:
            raise ValueError("Dataset not loaded. Call _load_dataset() first.")

        transformed_records = []
        for idx, record in enumerate(self.dataset):
            try:
                transformed = self.transform_record(record)
                transformed_records.append(transformed)
                if (idx + 1) % 100 == 0:
                    logger.info(f"Processed {idx + 1} records")
            except Exception as e:
                logger.warning(f"Failed to transform record {idx}: {e}")
                continue

        logger.info(f"Successfully transformed {len(transformed_records)} records")
        return transformed_records

    def save_to_yaml(self, records, output_path):
        """
        Save transformed records to a YAML file.

        Args:
            records: List[Dict[str, Any]]
                List of transformed LinkML entities
            output_path: str
                Path to save the YAML file
        """
        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)

        container_class = self.get_container_class_name()

        # Get the plural form of the class name (simple pluralization)
        # This assumes the LinkML model uses lowercase plurals
        entity_type = self._get_entity_type_plural()

        output_data = {
            entity_type: records
        }

        with open(output_path, 'w') as f:
            yaml.dump(output_data, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

        logger.info(f"Saved {len(records)} records to {output_path}")

    @abstractmethod
    def _get_entity_type_plural(self) -> str:
        """
        Get the plural name of the entity type for the YAML container.

        For example: "benchmarks", "evaluations", etc.

        Returns:
            The plural entity type name
        """
        pass

    def load_and_save(self, output_path: str) -> None:
        """
        Convenience method to load, transform, and save all records in one call.

        Args:
            output_path: Path to save the YAML file
        """
        records = self.load_and_transform()
        self.save_to_yaml(records, output_path)
        logger.info(f"Load and save complete: {len(records)} records saved to {output_path}")
