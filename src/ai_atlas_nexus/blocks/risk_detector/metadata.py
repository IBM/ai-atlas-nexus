from collections import Counter
from typing import Any, List, Union

from ai_atlas_nexus.ai_risk_ontology.datamodel.ai_risk_ontology import Risk
from ai_atlas_nexus.blocks.inference import TextGenerationInferenceOutput
from ai_atlas_nexus.blocks.inference.params import (
    InferenceMetadata,
    TokenUsage,
    UsecaseInferenceMetadata,
)
from ai_atlas_nexus.blocks.risk_detector.decorator import RiskDetectorDecorator
from ai_atlas_nexus.blocks.risk_detector.generic import DetectionRun
from ai_atlas_nexus.blocks.risk_detector.results import (
    DetectionResult,
    RiskWithExplanation,
)


class RiskDetectorWithMetadata(RiskDetectorDecorator):
    """Wraps a detector to report what the inference cost.

    `detect` returns the wrapped detector's results inside a `DetectionResult`,
    alongside token usage, call counts, stop reasons, seeds and whether the model
    produced thinking. Figures are reported both aggregated over the run and broken
    down per usecase.

    Wrap either a `GenericRiskDetector` or a `RiskDetectorWithExplanation`:

        >>> detector = RiskDetectorWithMetadata(GenericRiskDetector(...))
        >>> result = detector.detect(["my system"])
        >>> result.metadata.token_usage.total_tokens
        >>> result.metadata.per_usecase[0].token_usage.total_tokens
    """

    def detect(
        self, usecases: List[str]
    ) -> DetectionResult[Union[List[List[Risk]], List[List[RiskWithExplanation]]]]:
        """Identify risks from usecases and report the inference metadata.

        Args:
            usecases: List of usecase descriptions.

        Returns:
            The wrapped detector's results in `DetectionResult.data`, with aggregated
            and per-usecase inference metadata in `DetectionResult.metadata`.
        """
        run = self._run_inference(usecases)
        return DetectionResult(data=run.data, metadata=self._build_metadata(run))

    def _build_metadata(self, run: DetectionRun[Any]) -> InferenceMetadata:
        """Summarize the run as a whole, and each usecase within it."""
        overall = self._summarize(run.all_outputs)
        return InferenceMetadata(
            token_usage=overall.token_usage,
            inference_engine=str(self.inference_engine._inference_engine_type),
            model=self.inference_engine.model_name_or_path,
            num_calls=overall.num_calls,
            seed=overall.seed,
            stop_reason_summary=overall.stop_reason_summary,
            has_thinking=overall.has_thinking,
            per_usecase=[self._summarize(outputs) for outputs in run.outputs],
        )

    @staticmethod
    def _summarize(
        responses: List[TextGenerationInferenceOutput],
    ) -> UsecaseInferenceMetadata:
        """Reduce a set of inference responses to one metadata record."""
        seeds = {response.seed for response in responses}
        return UsecaseInferenceMetadata(
            # `TokenUsage.__post_init__` derives each total
            # `__add__` keeps unreported counts as None rather than fabricating a zero.
            token_usage=sum(
                (
                    TokenUsage(
                        input_tokens=response.input_tokens,
                        output_tokens=response.output_tokens,
                    )
                    for response in responses
                ),
                TokenUsage(),
            ),
            num_calls=len(responses),
            # Don't show the seed unless every call used it.
            seed=seeds.pop() if len(seeds) == 1 else None,
            stop_reason_summary=dict(
                Counter(
                    response.stop_reason
                    for response in responses
                    if response.stop_reason
                )
            ),
            has_thinking=any(response.thinking for response in responses),
        )
