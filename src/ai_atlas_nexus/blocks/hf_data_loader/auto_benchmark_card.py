"""
Loader for converting the Auto-BenchmarkCard HuggingFace dataset records into BenchmarkMetadataCard instances.
"""

from datetime import datetime
from typing import Any, Dict, Optional

from ai_atlas_nexus import AIAtlasNexus
from ai_atlas_nexus.blocks.hf_data_loader.base import HFDataLoaderBase
from ai_atlas_nexus.toolkit.logging import configure_logger


logger = configure_logger(__name__)


class AutoBenchmarkCardLoader(HFDataLoaderBase):
    """
    Loader for the IBM Auto-BenchmarkCard dataset. Converts records from the
    https://huggingface.co/datasets/ibm-research/Auto-BenchmarkCard
    dataset into BenchmarkMetadataCard instances.
    """

    def __init__(self, split = "train"):
        """
        Initialize the Auto-BenchmarkCard loader.

        Args:
            split: str
                The dataset split to use (default: "train")
        """
        self._nexus = AIAtlasNexus()
        super().__init__(
            dataset_name="ibm-research/Auto-BenchmarkCard",
            split=split,
            subset=None,

        )

    def transform_record(self, record):
        """
        Transform a HuggingFace Auto-BenchmarkCard record into a BenchmarkMetadataCard.

        Args:
            record:  Dict[str, Any]
                A single record from the Auto-BenchmarkCard dataset

        Returns:
            Dict[str, Any]
                A dictionary representing a BenchmarkMetadataCard
        """
        # Extract the nested benchmark card data
        benchmark_card = record.get("benchmark_card", {})
        if not benchmark_card:
            logger.warning("Record has no benchmark_card field, skipping record")
            return {}

        # Core fields from benchmark card
        metadata_card = {
            "id": "auto_benchmark_card_" + benchmark_card["benchmark_details"]["name"],
            "name": benchmark_card["benchmark_details"]["name"],
            "description": benchmark_card["benchmark_details"]["overview"],
            "type": "BenchmarkMetadataCard",
        }

        # Optional fields
        optional_mappings = [
            ("describesAiEval", ["data", "source"]),
            ("hasDataType", ["benchmark_details", "data_type"]),
            ("hasDomains", ["benchmark_details", "domains"]),
            ("hasLanguages", ["benchmark_details", "languages"]),
            ("hasTasks", ["purpose_and_intended_users", "tasks"]),
            ("hasDataSource", ["data", "source"]),
            ("hasDataSize", ["data", "size"]),
            ("hasDataFormat", ["data", "format"]),
            ("hasAnnotation", ["data", "annotation"]),
            ("hasMethods", ["methodology", "methods"]),
            ("hasMetrics", ["methodology","metrics"]),
            ("hasCalculation", ["methodology","calculation"]),
            ("hasInterpretation", ["methodology","interpretation"]),
            ("hasBaselineResults", ["methodology", "baseline_results"]),
            ("hasValidation", ["methodology","validation"]),
            ("hasLimitations", ["purpose_and_intended_users", "limitations"]),
            ("hasOutOfScopeUses", ["purpose_and_intended_users", "out_of_scope_uses"]),
            ("hasGoal", ["purpose_and_intended_users", "goal"]),
            ("hasAudience", ["purpose_and_intended_users","audience"]),
            ("hasResources", ["benchmark_details", "resources"]),
            ("hasSimilarBenchmarks", ["benchmark_details", "similar_benchmarks"]),
            ("hasConsiderationPrivacyAndAnonymity", ["ethical_and_legal_considerations", "privacy_and_anonymity"]),
            ("hasConsiderationConsentProcedures", ["ethical_and_legal_considerations", "consent_procedures"]),
            ("hasConsiderationComplianceWithRegulations", ["ethical_and_legal_considerations", "compliance_with_regulations"]),
            ("hasLicense", ["ethical_and_legal_considerations", "data_licensing"])

        ]

        for linkml_field, possible_source_fields in optional_mappings:
            value = self._get_nested_field(benchmark_card, *possible_source_fields)

            if value:
                metadata_card[linkml_field] = self._normalize_value(value)

        # related risks
        if benchmark_card["possible_risks"]:
            related_risks = [self._nexus.query("risk", name=risk["category"], isDefinedByTaxonomy="ibm-risk-atlas") for risk in benchmark_card["possible_risks"]]
            metadata_card["hasRelatedRisks"] = [item.id for sublist in related_risks for item in sublist]


        # Add metadata
        metadata_card["dateCreated"] = datetime.now().isoformat()

        return metadata_card

    def _generate_id(self, benchmark_card: Dict[str, Any]) -> str:
        """
        Generate a unique ID for the benchmark card.

        Args:
            benchmark_card: The benchmark_card nested object

        Returns:
            A unique ID string
        """
        # Try to get a name or identifier from the benchmark_card
        name = self._get_nested_field(benchmark_card, "name", "benchmark_name", "title", "id")

        if name:
            # Convert to lowercase and replace spaces/special chars with underscores
            clean_name = name.lower().replace(" ", "_").replace("-", "_")
            clean_name = "".join(c for c in clean_name if c.isalnum() or c == "_")
            return f"auto-benchmark-{clean_name}"
        else:
            # Fallback to timestamp-based ID
            import time
            return f"auto-benchmark-{int(time.time() * 1000)}"

    def _get_nested_field(self, obj: Dict[str, Any], *field_names: str) -> Optional[Any]:
        """
        Get a field value from a nested object, trying multiple possible field names.

        Args:
            obj: The nested object (typically benchmark_card)
            field_names: field name

        Returns:
            The field value if found, None otherwise
        """
        value = obj[field_names[0]][field_names[1]]
        return value


    def _normalize_value(self, value: Any) -> list:
        """
        Normalize a value to a list format for LinkML fields.

        Args:
            value: The value to normalize

        Returns:
            A list representation of the value
        """
        if isinstance(value, str):
            return [value]
        elif isinstance(value, list):
            return value
        elif isinstance(value, dict):
            # Convert dict values to list
            return list(value.values()) if value.values() else [str(value)]
        else:
            return [str(value)]

    def get_container_class_name(self) -> str:
        """Get the LinkML container class name."""
        return "Container"

    def _get_entity_type_plural(self) -> str:
        """Get the plural name for BenchmarkMetadataCard entities."""
        return "benchmarkmetadatacards"

    def load_and_save_benchmarks(self, output_path: str) -> None:
        """
        Load Auto-BenchmarkCard records and save as BenchmarkMetadataCard instances.

        Args:
            output_path: Path to save the YAML file containing benchmark metadata cards
        """
        logger.info(f"Loading Auto-BenchmarkCard dataset and saving to {output_path}")
        self.load_and_save(output_path)
