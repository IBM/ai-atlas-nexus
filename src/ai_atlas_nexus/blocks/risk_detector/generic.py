import json
from typing import List

from ai_atlas_nexus.ai_risk_ontology.datamodel.ai_risk_ontology import Risk
from ai_atlas_nexus.blocks.inference import TextGenerationInferenceOutput
from ai_atlas_nexus.blocks.prompt_response_schema import LIST_OF_STR_SCHEMA
from ai_atlas_nexus.blocks.prompt_templates import (
    RISK_IDENTIFICATION_BATCH_TEMPLATE,
    RISK_IDENTIFICATION_PER_RISK_DSPY_TEMPLATES,
    RISK_IDENTIFICATION_PER_RISK_TEMPLATE,
)
from ai_atlas_nexus.blocks.risk_detector import RiskDetector


class GenericRiskDetector(RiskDetector):

    def detect(self, usecases: List[str]) -> List[List[Risk]]:
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

        # Populate schema items
        json_schema = dict(LIST_OF_STR_SCHEMA)
        json_schema["items"]["enum"] = [risk.name for risk in self._risks]

        # Invoke inference service
        inference_responses: List[TextGenerationInferenceOutput] = (
            self.inference_engine.generate(
                prompts,
                response_format=json_schema,
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
        ]

    def detect_one(self, usecases: List[str]) -> List[List[Risk]]:
        all_risks = []
        for usecase in usecases:
            prompts = [
                self.prompt_builder(
                    prompt_template=(
                        RISK_IDENTIFICATION_PER_RISK_DSPY_TEMPLATES.get(
                            self.inference_engine.model_name_or_path,
                            RISK_IDENTIFICATION_PER_RISK_TEMPLATE,
                        )
                        if self.use_dspy_prompt
                        else RISK_IDENTIFICATION_PER_RISK_TEMPLATE
                    )
                ).build(
                    cot_examples=self._examples,
                    usecase=usecase,
                    risk_name=risk.name,
                    risk_description=risk.description,
                )
                for risk in self._risks
            ]

            # Populate schema items
            json_schema = dict(LIST_OF_STR_SCHEMA)
            json_schema["items"]["enum"] = ["Yes", "No"]

            # Invoke inference service
            inference_responses: List[TextGenerationInferenceOutput] = (
                self.inference_engine.generate(
                    prompts,
                    response_format={
                        "type": "object",
                        "properties": {
                            "answer": {
                                "type": "string",
                                "enum": ["Yes", "No"],
                            },
                            "explanation": {"type": "string"},
                        },
                        "required": ["answer", "explanation"],
                    },
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
