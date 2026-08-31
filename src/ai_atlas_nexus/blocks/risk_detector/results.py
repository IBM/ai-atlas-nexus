import dataclasses
from typing import Generic, Optional, TypeVar

from ai_atlas_nexus.ai_risk_ontology.datamodel.ai_risk_ontology import Risk
from ai_atlas_nexus.blocks.inference.params import InferenceMetadata


T = TypeVar("T")


@dataclasses.dataclass(kw_only=True)
class RiskWithExplanation:
    """Risk object and an explanation of why it was identified.

    Attributes:
        risk: The Risk object.
        explanation: Explanation text, source depends on the `ExplanationType`
            requested. None when the model supplied none.
    """

    risk: Risk
    explanation: Optional[str] = None


@dataclasses.dataclass(kw_only=True)
class DetectionResult(Generic[T]):
    """Detection results paired with metadata about the inference

    Attributes:
        data: The detected items, e.g. `List[List[Risk]]` or
            `List[List[RiskWithExplanation]]`.
        metadata: Token usage and call information, aggregated over the run and
            broken down per usecase.
    """

    data: T
    metadata: InferenceMetadata
