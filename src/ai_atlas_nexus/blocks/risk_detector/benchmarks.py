import json
from typing import List

from ai_atlas_nexus.ai_risk_ontology.datamodel.ai_risk_ontology import Risk
from ai_atlas_nexus.blocks.inference import TextGenerationInferenceOutput
from ai_atlas_nexus.blocks.prompt_response_schema import LIST_OF_STR_SCHEMA
from ai_atlas_nexus.blocks.risk_detector import RiskDetector


# Benchmark-specific risk identification template
BENCHMARK_RISK_IDENTIFICATION_TEMPLATE = """You are an expert at AI risk classification for AI benchmarks and evaluation datasets.

A benchmark is a standardized dataset and evaluation protocol used to measure AI model capabilities. Risks of a benchmark are about what can go wrong when this benchmark is USED to evaluate models — not risks of deploying AI in general.

Think about:
- **Data risks**: What biases, gaps, or quality issues exist in the benchmark's data? Could the data source introduce systematic biases? Is the data representative?
- **Evaluation risks**: Could benchmark scores be misleading? Could models game the metric? Does the benchmark adequately measure what it claims to? Could results be misinterpreted?
- **Misuse risks**: Could this benchmark be used to develop or validate harmful capabilities? Could good performance on this benchmark give false confidence?
- **Transparency risks**: Is the benchmark's methodology, data provenance, and scoring well-documented? Can results be reproduced?

IMPORTANT: Only select risks that are specifically relevant to THIS benchmark based on its description, data, and methodology. Do NOT select generic risks that apply to all AI systems equally.

Study the risk categories below:

RISKS:
{{ risks }}

{% if cot_examples is not none and cot_examples|length > 0 %}
EXAMPLES — study how risks are matched to benchmarks based on their specific characteristics:
{% for example in cot_examples %}
Benchmark: {{ example.Usecase }}
Reasoning: {{ example.Reasoning }}
Risks: {{ example.Risks }}
{% endfor %}
===== END OF EXAMPLES ======
{% endif %}
Now identify risks for the following benchmark. Think step by step about which risks apply based on the benchmark's specific characteristics.

Benchmark: {{ usecase }}

Respond with an array list{% if max_risk is not none %} (top {{ max_risk }} most relevant risk categories){% endif %} of attribute 'category' containing the risk labels.
Risks: """


class BenchmarkRiskDetector(RiskDetector):

    def detect(self, usecases: List[str]) -> List[List[Risk]]:
        prompts = [
            self.prompt_builder(
                prompt_template=BENCHMARK_RISK_IDENTIFICATION_TEMPLATE
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
        inference_response: List[TextGenerationInferenceOutput] = (
            self.inference_engine.generate(
                prompts,
                response_format=json_schema,
                postprocessors=["list_of_str"],
            )
        )

        return [
            list(
                filter(
                    lambda risk: risk.name in inference.prediction,
                    self._risks,
                )
            )
            for inference in inference_response
        ]
