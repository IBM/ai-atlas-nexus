"""A single inference-engine stub for tests
"""

import dataclasses
from typing import Any, List, NamedTuple, Optional, Sequence

from ai_atlas_nexus.blocks.inference import InferenceEngine
from ai_atlas_nexus.blocks.inference.params import TextGenerationInferenceOutput


class StubResponse(NamedTuple):
    prediction: Any
    input_tokens: Optional[int] = 100
    output_tokens: Optional[int] = 10
    stop_reason: Optional[str] = None
    seed: Optional[int] = None
    thinking: Optional[str] = None


@dataclasses.dataclass
class StubCall:
    """What one `generate` call was asked for."""

    prompts: List[str]
    response_format: Any = None
    postprocessors: Optional[List[str]] = None


class StubInferenceEngine(InferenceEngine):
    """Serves canned responses and records the calls.

    `InferenceEngine.__init__` is bypassed on purpose: it builds a real backend
    client. Only the attributes detectors read are set.

    Responses are consumed in order across calls, so this stub covers both the
    batch path (one call, one prompt per usecase) and the per-risk path (one call
    per usecase, one prompt per risk).
    """

    # A stub is not one of the real engine types, but the label is only ever
    # stringified for reporting, so a plain string stands in for one.
    _inference_engine_type: str

    def __init__(
        self,
        responses: Sequence[StubResponse],
        model_name_or_path: str = "stub-model",
        engine_type: str = "STUB",
    ):
        self._responses = list(responses)
        self._served = 0
        self.model_name_or_path = model_name_or_path
        self._inference_engine_type = engine_type
        self.calls: List[StubCall] = []

    def prepare_credentials(self, credentials=None):
        return {}

    def create_client(self, credentials=None):
        return None

    def chat(self, *args, **kwargs):
        raise NotImplementedError("tests do not exercise the chat path")

    def generate(
        self, prompts, response_format=None, postprocessors=None, **kwargs
    ) -> List[TextGenerationInferenceOutput]:
        prompts = list(prompts)
        self.calls.append(
            StubCall(
                prompts=prompts,
                response_format=response_format,
                postprocessors=postprocessors,
            )
        )

        served = self._responses[self._served : self._served + len(prompts)]
        # Returning fewer responses than prompts would silently misalign risks with
        # responses, which is exactly what these tests are checking.
        assert len(served) == len(prompts), (
            f"stub has {len(served)} response(s) left but was given {len(prompts)} "
            f"prompt(s); add more StubResponse entries"
        )
        self._served += len(prompts)

        return [
            TextGenerationInferenceOutput(
                prediction=response.prediction,
                input_tokens=response.input_tokens,
                output_tokens=response.output_tokens,
                stop_reason=response.stop_reason,
                seed=response.seed,
                thinking=response.thinking,
                inference_engine=self._inference_engine_type,
                model_name_or_path=self.model_name_or_path,
            )
            for response in served
        ]
