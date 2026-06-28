"""
Loader for converting the Every Eval Ever HuggingFace dataset records into EveryEvalAIResult instances.
"""

from datetime import datetime
from typing import Any, Optional

from ai_atlas_nexus import AIAtlasNexus
from ai_atlas_nexus.ai_risk_ontology.datamodel.ai_risk_ontology import (
    EvaluationResultRecord,
    EveryEvalAIResult,
    MetricConfig,
    ModelInfo,
    ScoreDetails,
    SourceData,
    SourceMetadata,
)
from ai_atlas_nexus.blocks.hf_data_loader.base import HFDataLoaderBase
from ai_atlas_nexus.toolkit.logging import configure_logger


logger = configure_logger(__name__)


class EveryEvalEverLoader(HFDataLoaderBase):
    """
    Loader for the Every Eval Ever dataset. Converts records from the
    https://huggingface.co/datasets/evaleval/EEE_datastore
    dataset into EveryEvalAIResult instances.
    """

    def __init__(self, subset=None, split="train"):
        """
        Initialize the Every Eval Ever loader.

        Args:
            subset: Optional[str]
                The dataset subset/configuration to use (e.g., "global-mmlu-lite")
            split: str
                The dataset split to use (default: "train")
        """
        self._nexus = AIAtlasNexus()
        super().__init__(
            dataset_name="evaleval/EEE_datastore",
            split=split,
            subset=subset,
        )

    def transform_record(self, record) -> Optional[EveryEvalAIResult]:
        """
        Transform a HuggingFace Every Eval Ever record into an EveryEvalAIResult.

        Args:
            record:  Dict[str, Any]
                A single record from the Every Eval Ever dataset

        Returns:
            Optional[EveryEvalAIResult]
                An EveryEvalAIResult instance, or None if evaluation_id is missing
        """
        # Core fields
        evaluation_id = record.get("evaluation_id", "")

        if not evaluation_id:
            logger.warning("Record has no evaluation_id field, skipping record")
            return None

        # Transform source_metadata
        source_metadata_obj = None
        source_metadata = record.get("source_metadata", {})
        if source_metadata:
            source_metadata_obj = SourceMetadata(
                id=f"{evaluation_id}_source_metadata",
                source_name=source_metadata.get("source_name", None),
                source_type=source_metadata.get("source_type", None),
                source_organization_name=source_metadata.get("source_organization_name", None),
                source_organization_url=source_metadata.get("source_organization_url", None),
                evaluator_relationship=source_metadata.get("evaluator_relationship", None),
            )

        # Transform model_info
        model_info_obj = None
        model_info = record.get("model_info", None)
        if model_info:
            model_info_obj = ModelInfo(
                id=f"{evaluation_id}_model_info",
                model_name=model_info.get("name", None),
                model_id=model_info.get("id", None),
            )

        # Transform evaluation_results array
        evaluation_results_dict = None
        evaluation_results = record.get("evaluation_results", [])
        if evaluation_results:
            transformed_results: dict[str, EvaluationResultRecord] = {}
            for idx, eval_record in enumerate(evaluation_results):
                key = f"{evaluation_id}_result_{idx}"

                # Transform source_data
                source_data_obj = None
                source_data = eval_record.get("source_data", {})
                if source_data:
                    source_data_obj = SourceData(
                        id=f"{evaluation_id}_result_{idx}_source_data",
                        dataset_name=source_data.get("dataset_name", None),
                        source_type=source_data.get("source_type", None),
                        hf_repo=source_data.get("hf_repo", None),
                        hf_split=source_data.get("hf_split", None),
                    )

                # Transform metric_config
                metric_config_obj = None
                metric_config = eval_record.get("metric_config", {})
                if metric_config:
                    metric_config_obj = MetricConfig(
                        id=f"{evaluation_id}_result_{idx}_metric_config",
                        lower_is_better=metric_config.get("lower_is_better", False),
                        score_type=metric_config.get("score_type", None),
                        min_score=metric_config.get("min_score", 0.0),
                        max_score=metric_config.get("max_score", 1.0),
                    )

                # Transform score_details
                score_details_obj = None
                score_details = eval_record.get("score_details", {})
                if score_details:
                    score_details_obj = ScoreDetails(
                        id=f"{evaluation_id}_result_{idx}_score_details",
                        score=score_details.get("score", 0.0),
                    )

                transformed_results[key] = EvaluationResultRecord(
                    id=key,
                    evaluation_name=eval_record.get("evaluation_name", None),
                    hasSourceData=source_data_obj,
                    hasMetricConfig=metric_config_obj,
                    hasScoreDetails=score_details_obj,
                )

            if transformed_results:
                evaluation_results_dict = transformed_results

        return EveryEvalAIResult(
            id=f"eee_{evaluation_id}",
            value="",
            schema_version=record.get("schema_version", "1.0"),
            evaluation_id=evaluation_id,
            evaluation_timestamp=record.get("evaluation_timestamp"),
            retrieved_timestamp=record.get("retrieved_timestamp"),
            hasSourceMetadata=source_metadata_obj,
            hasModelInfo=model_info_obj,
            hasEvaluationResults=evaluation_results_dict,
            dateCreated=datetime.now().date(),
        )

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
        """Get the plural name for EveryEvalAIResult entities."""
        return "everyevalaresults"

    def load_and_save_evaluations(self, output_path: str) -> None:
        """
        Load Every Eval Ever records and save as EveryEvalAIResult instances.

        Args:
            output_path: Path to save the YAML file containing evaluation results
        """
        logger.info(f"Loading Every Eval Ever dataset and saving to {output_path}")
        self.load_and_save(output_path)
