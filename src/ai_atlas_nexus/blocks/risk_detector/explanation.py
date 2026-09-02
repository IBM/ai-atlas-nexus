from typing import List, Literal, Optional

from pydantic import create_model

from ai_atlas_nexus.ai_risk_ontology.datamodel.ai_risk_ontology import Risk
from ai_atlas_nexus.blocks.inference import TextGenerationInferenceOutput
from ai_atlas_nexus.blocks.risk_detector.decorator import RiskDetectorDecorator
from ai_atlas_nexus.blocks.risk_detector.generic import (
    BatchSchema,
    DetectionRun,
    GenericRiskDetector,
)
from ai_atlas_nexus.blocks.risk_detector.results import RiskWithExplanation
from ai_atlas_nexus.metadata_base import ExplanationType


class RiskDetectorWithExplanation(RiskDetectorDecorator):
    """Wraps a detector to pair each identified risk with an explanation.

    `detect` returns `RiskWithExplanation` items.
    `ExplanationType` dictates the source of explanation:

        DESCRIPTION       the risk's description from the ontology
        REASONING         the model's thinking, for models that expose it
        SELF_EXPLANATION  the model's own justification, which it is asked for by
                          extending the response schema

    Usage:

        >>> detector = RiskDetectorWithExplanation(
        ...     GenericRiskDetector(...), ExplanationType.DESCRIPTION
        ... )
        >>> for explained in detector.detect(["my system"])[0]:
        ...     print(explained.risk.name, explained.explanation)
    """

    _detector: GenericRiskDetector

    def __init__(
        self, detector: GenericRiskDetector, explanation_type: ExplanationType
    ):
        """
        Args:
            detector: The detector whose results to annotate.
            explanation_type: Where each explanation should come from. An
                `ExplanationType`, or any value accepted by it such as
                `"description"`. `NONE` is rejected.

        Raises:
            ValueError: If `explanation_type` is unknown or `ExplanationType.NONE`.
            TypeError: If `detector` is not a `GenericRiskDetector`.
        """
        if not isinstance(detector, GenericRiskDetector):
            raise TypeError(
                f"`RiskDetectorWithExplanation` must wrap a `GenericRiskDetector`, not "
                f"{type(detector).__name__}: it asks that detector for a response "
                f"schema carrying explanations. This decorator goes innermost, e.g. "
                f"`RiskDetectorWithMetadata(RiskDetectorWithExplanation(detector, ...))`."
            )

        try:
            explanation_type = ExplanationType(explanation_type)
        except ValueError:
            raise ValueError(
                f"Unknown explanation type: {explanation_type!r}. Expected one of "
                f"{[member.value for member in ExplanationType]}."
            ) from None

        if explanation_type is ExplanationType.NONE:
            raise ValueError(
                "`RiskDetectorWithExplanation` needs an explanation type other than "
                "`ExplanationType.NONE`. To detect risks without explanations, use the "
                "wrapped detector directly."
            )

        super().__init__(detector)
        self._explanation_type = explanation_type

    def detect(self, usecases: List[str]) -> List[List[RiskWithExplanation]]:
        """Identify risks from usecases, each paired with an explanation.

        Args:
            usecases: List of usecase descriptions to analyze.

        Returns:
            One list of `RiskWithExplanation` per usecase. An explanation is None when
            the model did not supply one, which the requested type allows.
        """
        return self._run_inference(usecases).data

    def _run_inference(
        self, usecases: List[str], batch_schema: Optional[BatchSchema] = None
    ) -> DetectionRun[RiskWithExplanation]:
        run = super()._run_inference(
            usecases, batch_schema=batch_schema or self._batch_schema_override()
        )
        return DetectionRun(
            data=[
                [
                    RiskWithExplanation(
                        risk=risk, explanation=self._explain(risk, source)
                    )
                    for risk, source in zip(risks, sources)
                ]
                for risks, sources in zip(run.data, run.sources)
            ],
            sources=run.sources,
            outputs=run.outputs,
        )

    def _batch_schema_override(self) -> Optional[BatchSchema]:
        """Response schema override for the wrapped detector's batch path.
        """
        if self._explanation_type != ExplanationType.SELF_EXPLANATION:
            return None

        risk_names = tuple(risk.name for risk in self._detector._risks if risk.name)
        if not risk_names:
            return None

        return BatchSchema(
            response_format=create_model(
                "RiskListWithExplanations",
                risks=(
                    List[
                        create_model(
                            "RiskWithExplanationItem",
                            risk_name=(Literal[risk_names], ...),
                            explanation=(str, ...),
                            __base__=None,
                        )
                    ],
                    ...,
                ),
                __base__=None,
            ),
            postprocessor="json_object",
        )

    def _explain(
        self, risk: Risk, inference_response: TextGenerationInferenceOutput
    ) -> Optional[str]:
        """Resolve one risk's explanation from the response that identified it."""
        if self._explanation_type == ExplanationType.DESCRIPTION:
            return risk.description
        if self._explanation_type == ExplanationType.REASONING:
            return inference_response.thinking
        if self._explanation_type == ExplanationType.SELF_EXPLANATION:
            return self._self_explanation(risk, inference_response)
        raise ValueError(f"No explanation source for {self._explanation_type!r}")

    @staticmethod
    def _self_explanation(
        risk: Risk, inference_response: TextGenerationInferenceOutput
    ) -> Optional[str]:
        """Extract the risk's explanation from the model's own response.
        """
        prediction = inference_response.prediction
        if not isinstance(prediction, dict):
            return None

        items = prediction.get("risks")
        if isinstance(items, list):
            return next(
                (
                    item.get("explanation")
                    for item in items
                    if isinstance(item, dict) and item.get("risk_name") == risk.name
                ),
                None,
            )

        return prediction.get("explanation")
