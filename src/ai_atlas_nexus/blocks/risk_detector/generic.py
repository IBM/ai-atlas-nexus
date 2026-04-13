import json
from typing import List, Literal

from pydantic import create_model

from ai_atlas_nexus.ai_risk_ontology.datamodel.ai_risk_ontology import Risk
from ai_atlas_nexus.blocks.inference import TextGenerationInferenceOutput
from ai_atlas_nexus.blocks.prompt_response_schema import AIRiskPresence
from ai_atlas_nexus.blocks.prompt_templates import (
    RISK_IDENTIFICATION_BATCH_TEMPLATE,
    RISK_IDENTIFICATION_PER_RISK_DSPY_TEMPLATES,
    RISK_IDENTIFICATION_PER_RISK_TEMPLATE,
)
from ai_atlas_nexus.blocks.risk_detector import RiskDetector
from ai_atlas_nexus.toolkit.logging import configure_logger


logger = configure_logger(__name__)


class GenericRiskDetector(RiskDetector):

    def detect(self, usecases: List[str]) -> List[List[Risk]]:
        return (
            self.detect_one(usecases)
            if self.use_dspy_prompt or not self.batch_inference
            else self.detect_batch(usecases)
        )

    def detect_batch(self, usecases: List[str]) -> List[List[Risk]]:
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
                response_format=create_model(
                    "AIRisk",
                    risks=(List[Literal[tuple([risk.name for risk in self._risks])]]),
                ),
                postprocessors=["list_of_str"],
            )
        )

        return [
            (
                list(
                    filter(
                        lambda risk: risk.name in inference_response.prediction,
                        self._risks,
                    )
                )
                if inference_response.prediction
                else []
            )
            for inference_response in inference_responses
        ][: self.max_risk]

    def detect_one(self, usecases: List[str]) -> List[List[Risk]]:
        all_risks = []

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

            all_risks.append(
                [
                    self._risks[index]
                    for index, response in enumerate(inference_responses)
                    if response.prediction["answer"] == "Yes"
                ]
            )

        return all_risks
