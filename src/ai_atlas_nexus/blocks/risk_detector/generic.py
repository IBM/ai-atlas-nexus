import dataclasses
import json
from typing import Any, Generic, List, NamedTuple, Optional, TypeVar, Union

from ai_atlas_nexus.ai_risk_ontology.datamodel.ai_risk_ontology import Risk
from ai_atlas_nexus.blocks.inference import TextGenerationInferenceOutput
from ai_atlas_nexus.blocks.prompt_response_schema import (
    LIST_OF_STR_SCHEMA,
    AIRiskPresence,
)
from ai_atlas_nexus.blocks.prompt_templates import (
    RISK_IDENTIFICATION_BATCH_TEMPLATE,
    RISK_IDENTIFICATION_PER_RISK_DSPY_TEMPLATES,
    RISK_IDENTIFICATION_PER_RISK_TEMPLATE,
)
from ai_atlas_nexus.blocks.risk_detector.base import RiskDetector
from ai_atlas_nexus.toolkit.logging import configure_logger


logger = configure_logger(__name__)


T = TypeVar("T")


class BatchSchema(NamedTuple):
    """A batch response schema with the postprocessor that parses its output."""

    response_format: Any
    postprocessor: str


@dataclasses.dataclass(kw_only=True)
class DetectionRun(Generic[T]):
    """One detection pass.

    Attributes:
        data: Detected items per usecase.
        sources: Parallel to `data`: `sources[i][j]` is the inference output that
            identified `data[i][j]`. In batch mode every item in a usecase shares
            the one response; in per-risk mode each item has its own.
        outputs: Every inference output produced by the run, grouped by usecase and
            in call order. (Note this includes calls that identified
            nothing, because they still cost tokens.)
    """

    data: List[List[T]]
    sources: List[List[TextGenerationInferenceOutput]]
    outputs: List[List[TextGenerationInferenceOutput]]

    @property
    def all_outputs(self) -> List[TextGenerationInferenceOutput]:
        """Every inference output in the run, flattened, in call order."""
        return [
            output for usecase_outputs in self.outputs for output in usecase_outputs
        ]


class GenericRiskDetector(RiskDetector):

    def detect(self, usecases: List[str]) -> List[List[Risk]]:
        """Identify risks from usecases.

        Args:
            usecases: List of usecase descriptions to analyze.

        Returns:
            One list of `Risk` per usecase, in the order the usecases were passed in.

        Examples:
            >>> for risks in detector.detect(["my system"]):
            ...     for risk in risks:
            ...         print(risk.name)

            To pair each risk with an explanation, or to report what the inference
            cost, wrap the detector:

            >>> RiskDetectorWithExplanation(detector, explanation_type).detect(...)
            >>> RiskDetectorWithMetadata(detector).detect(...)
        """
        return self._run_inference(usecases).data

    def _run_inference(
        self, usecases: List[str], batch_schema: Optional[BatchSchema] = None
    ) -> DetectionRun[Risk]:
        """Run detection and return the risks together with their raw inference outputs.

        Args:
            usecases: List of usecase descriptions to analyze.
            batch_schema: Overrides the batch response schema and its postprocessor.
        """
        if self.use_dspy_prompt or not self.batch_inference:
            return self._run_per_risk(usecases)
        return self._run_batch(usecases, batch_schema or self._batch_schema())

    def _batch_schema(self) -> BatchSchema:
        """Response schema and postprocessor for the batch prompt.
        """
        return BatchSchema(
            response_format={
                **LIST_OF_STR_SCHEMA,
                "items": {
                    **LIST_OF_STR_SCHEMA["items"],
                    "enum": [risk.name for risk in self._risks],
                },
            },
            postprocessor="list_of_str",
        )

    def _run_batch(
        self, usecases: List[str], batch_schema: BatchSchema
    ) -> DetectionRun[Risk]:
        prompts = [
            self.prompt_builder(
                prompt_template=RISK_IDENTIFICATION_BATCH_TEMPLATE
            ).build(
                cot_examples=self._examples,
                usecase=usecase,
                risks=json.dumps(
                    [
                        {"category": risk.name, "description": risk.description}
                        for risk in self._risks
                    ],
                    indent=4,
                ),
                max_risk=self.max_risk,
            )
            for usecase in usecases
        ]

        # Invoke inference service
        inference_responses: List[TextGenerationInferenceOutput] = (
            self.inference_engine.generate(
                prompts,
                response_format=batch_schema.response_format,
                postprocessors=[batch_schema.postprocessor],
            )
        )

        known_names = {risk.name for risk in self._risks if risk.name}
        risks_data = []
        sources = []
        for inference_response in inference_responses:
            predicted_risk_names = self._extract_risk_predictions(
                inference_response.prediction
            )
            ranked = []
            for name in predicted_risk_names:
                if isinstance(name, str) and name in known_names and name not in ranked:
                    ranked.append(name)
            top = ranked[: self.max_risk]
            identified = [risk for risk in self._risks if risk.name in top]
            risks_data.append(identified)
            # One response covers every risk it named.
            sources.append([inference_response] * len(identified))

        return DetectionRun(
            data=risks_data,
            sources=sources,
            # The batch path makes exactly one call per usecase.
            outputs=[[response] for response in inference_responses],
        )

    def _run_per_risk(self, usecases: List[str]) -> DetectionRun[Risk]:
        all_risks = []
        all_sources = []
        all_responses = []

        prompt_template = RISK_IDENTIFICATION_PER_RISK_TEMPLATE
        if self.use_dspy_prompt:
            for (
                model_ids,
                template,
            ) in RISK_IDENTIFICATION_PER_RISK_DSPY_TEMPLATES.items():
                if self.inference_engine.model_name_or_path in model_ids:
                    prompt_template = template
                    break

        for usecase in usecases:
            prompts = [
                self.prompt_builder(prompt_template=prompt_template).build(
                    cot_examples=self._examples,
                    usecase=usecase,
                    risk_name=risk.name,
                    risk_description=risk.description,
                )
                for risk in self._risks
            ]

            # Invoke inference service
            inference_responses: List[TextGenerationInferenceOutput] = (
                self.inference_engine.generate(
                    prompts,
                    response_format=AIRiskPresence,
                    postprocessors=["json_object"],
                )
            )
            all_responses.append(list(inference_responses))

            identified_risks = [
                (self._risks[index], response)
                for index, response in enumerate(inference_responses)
                if self._is_risk_present(response)
            ]
            all_risks.append([risk for risk, _ in identified_risks])
            all_sources.append([response for _, response in identified_risks])

        return DetectionRun(data=all_risks, sources=all_sources, outputs=all_responses)

    @staticmethod
    def _is_risk_present(response: TextGenerationInferenceOutput) -> bool:
        """Whether a per-risk response answered yes."""
        prediction = response.prediction
        if isinstance(prediction, dict) and "answer" in prediction:
            return prediction["answer"].lower() == "yes"
        # Postprocessing can be skipped or fail, leaving the raw model output.
        return isinstance(prediction, str) and "yes" in prediction.lower()

    def _extract_risk_predictions(
        self, prediction: Union[str, List[dict], dict, None]
    ) -> List[Any]:
        """Extract risk names from a prediction.

        Handles the list, dict and raw string shapes responses arrive in.
        """
        if isinstance(prediction, dict):
            # Handle dict format with "risks" or similar key
            risks = prediction.get("risks")
            if isinstance(risks, list):
                names = []
                for item in risks:
                    name = item.get("risk_name") if isinstance(item, dict) else item
                    if name is not None:
                        names.append(name)
                return names
            return []
        elif isinstance(prediction, list):
            return prediction
        elif isinstance(prediction, str):
            # In case postprocessing can be skipped or fail,  fall back to
            # substring matching so those responses still yield risks.
            return [
                risk.name
                for risk in self._risks
                if risk.name and risk.name in prediction
            ]
        return []
