from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional

from ai_atlas_nexus.ai_risk_ontology.datamodel.ai_risk_ontology import (
    Container,
    Risk,
    RiskTaxonomy,
)
from ai_atlas_nexus.blocks.inference.base import InferenceEngine
from ai_atlas_nexus.blocks.prompt_builder import (
    FewShotPromptBuilder,
    ZeroShotPromptBuilder,
)
from ai_atlas_nexus.data import load_resource
from ai_atlas_nexus.toolkit.logging import configure_logger
from ai_atlas_nexus.toolkit.validator import validate


LOGGER = configure_logger(__name__)


RISK_IDENTIFICATION_COT = load_resource("risk_generation_cot.json")
RISK_IDENTIFICATION_COT_SCHEMA = load_resource("risk_generation_cot_schema.json")


class RiskDetector(ABC):

    def __init__(
        self,
        risks: List[Risk],
        inference_engine: InferenceEngine,
        cot_examples: Optional[Dict[str, List]] = None,
        max_risk: Optional[int] = None,
    ):
        self.inference_engine = inference_engine
        self._risks = risks
        self._examples = cot_examples

        # Validate format of user-provided `cot_examples` if available
        if cot_examples is not None and (
            errors := validate(cot_examples, RISK_IDENTIFICATION_COT_SCHEMA)
        ):
            raise Exception(
                f"The format of `cot_examples` is incorrect. {errors}. Please refer to the example template provided "
                f"at src/ai_atlas_nexus/data/templates/risk_generation_cot.json"
            )

        # Set prompt builder based on whether the CoT examples are available.
        if self._examples is None:
            self.prompt_builder = ZeroShotPromptBuilder
        else:
            self.prompt_builder = FewShotPromptBuilder

        self.max_risk = max_risk

    def get_risks_by_taxonomy_id(
        self, ontology: Container, taxonomy_id: Optional[str] = None
    ):
        taxonomies = list(
            filter(
                lambda taxonomy: taxonomy.id == taxonomy_id,
                ontology.taxonomies,
            )
        )

        if len(taxonomies) > 0:
            taxonomy: RiskTaxonomy = taxonomies[0]
            LOGGER.info(
                f"Selected taxonomy is {str(taxonomy.name)}. For more info: {taxonomy.url}"
            )

            return list(
                filter(
                    lambda risk: risk.isDefinedByTaxonomy == taxonomy.id,
                    ontology.risks,
                )
            )
        else:
            raise Exception(
                f"Risk Taxonomy: {taxonomy_id} not found. Available taxonomies: "
                f"{[taxonomy.id for taxonomy in ontology.taxonomies]}"
            )

    @abstractmethod
    def detect(self, usecases: List[str]) -> List[List[Risk]]:
        raise NotImplementedError
