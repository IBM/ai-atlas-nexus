import copy
import json
from typing import List, NamedTuple

from ai_atlas_nexus.ai_risk_ontology.datamodel.ai_risk_ontology import Risk
from ai_atlas_nexus.blocks.inference import TextGenerationInferenceOutput
from ai_atlas_nexus.blocks.risk_detector import RiskDetector
from ai_atlas_nexus.toolkit.logging import configure_logger


logger = configure_logger(__name__)


class RiskRelation(NamedTuple):
    """A candidate risk and its SKOS mapping predicate to the source risk."""

    risk: Risk
    predicate: str


# The SKOS predicates used for cross-taxonomy mappings, strongest first. The
# directional broad/narrow predicates are intentionally excluded here: they are
# used for matches within a single taxonomy, whereas the risk mapper produces
# cross-taxonomy mappings.
RELATION_PREDICATES = {
    "exactMatch": "skos:exactMatch",
    "closeMatch": "skos:closeMatch",
    "relatedMatch": "skos:relatedMatch",
}


# Relation-classification template. Given a source risk and a set of candidate
# risks from other taxonomies, the model returns the SKOS relation for each
# candidate that is genuinely related, and omits the rest.
RISK_RELATION_IDENTIFICATION_TEMPLATE = """You are an expert at mapping AI risks across different risk taxonomies.

You are given a source risk and a list of candidate risks from other taxonomies. For each candidate that is genuinely related to the source risk, classify the relationship using one of these SKOS mapping predicates:

- exactMatch: the two risks describe the same risk and can be used interchangeably.
- closeMatch: the two risks are very similar and can be used interchangeably in many, but not all, applications.
- relatedMatch: the two risks are associated or overlap, but are not close enough to substitute for one another.

Only include candidates that are at least a relatedMatch. Omit any candidate that is unrelated to the source risk.

CANDIDATE RISKS:
{{ risks }}

{% if cot_examples is not none and cot_examples|length > 0 %}
EXAMPLES:
{% for example in cot_examples %}
Source risk: {{ example.Usecase }}
Reasoning: {{ example.Reasoning }}
Risks: {{ example.Risks }}
{% endfor %}
===== END OF EXAMPLES ======
{% endif %}
Now classify the relationship between the following source risk and the candidate risks. Think step by step.

Source risk: {{ usecase }}

Respond with a JSON array of objects, each having 'category' (the candidate risk name, exactly as listed) and 'relation' (one of exactMatch, closeMatch, relatedMatch). Include only related candidates.
JSON: """


# Array-of-objects response schema. The candidate names are populated per call.
RISK_RELATION_SCHEMA = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "category": {"type": "string", "enum": None},
            "relation": {
                "type": "string",
                "enum": list(RELATION_PREDICATES.keys()),
            },
        },
        "required": ["category", "relation"],
    },
}


class RiskRelationDetector(RiskDetector):
    """Classify the SKOS relation between a source risk and candidate risks.

    Unlike the other detectors, ``detect`` returns, for each source risk, a
    list of :class:`RiskRelation` (candidate risk + SKOS predicate) rather than
    a bare list of risks, so the risk mapper can emit a graded ``predicate_id``
    instead of a single hardcoded value.
    """

    def detect(self, usecases: List[str]) -> List[List[RiskRelation]]:
        prompts = [
            self.prompt_builder(
                prompt_template=RISK_RELATION_IDENTIFICATION_TEMPLATE
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
            )
            for usecase in usecases
        ]

        json_schema = copy.deepcopy(RISK_RELATION_SCHEMA)
        json_schema["items"]["properties"]["category"]["enum"] = [
            risk.name for risk in self._risks
        ]

        inference_responses: List[TextGenerationInferenceOutput] = (
            self.inference_engine.generate(
                prompts,
                response_format=json_schema,
                postprocessors=["json_object"],
            )
        )

        risks_by_name = {risk.name: risk for risk in self._risks}
        results: List[List[RiskRelation]] = []
        for response in inference_responses:
            prediction = response.prediction
            relations: List[RiskRelation] = []
            if isinstance(prediction, list):
                for item in prediction:
                    if not isinstance(item, dict):
                        continue
                    name = item.get("category")
                    relation = item.get("relation")
                    if name in risks_by_name and relation in RELATION_PREDICATES:
                        relations.append(
                            RiskRelation(
                                risks_by_name[name], RELATION_PREDICATES[relation]
                            )
                        )
            results.append(relations)

        return results
