from typing import List, Literal

from pydantic import BaseModel, Field

from ai_atlas_nexus.ai_risk_ontology.datamodel.ai_risk_ontology import EuAiRiskCategory


LIST_OF_STR_SCHEMA = {
    "type": "array",
    "items": {"enum": None},
}


class QuestionnaireOutput(BaseModel):
    """Questionnaire Response Schema"""

    answer: str = Field(description="Answer to the question.")
    explanation: str = Field(
        description="A brief two-sentence explanation on how that answer was generated"
    )
    confidence: Literal[
        "Likely answer from the intent", "Directly from the input text"
    ] = Field(description="Confidence in answering the question.")


class AIRiskPresence(BaseModel):
    """AI Risk Response Schema"""

    answer: Literal["Yes", "No"]
    explanation: str = Field(description="Explanation for having the given ai risk.")


class AITask(BaseModel):
    """AI Task Response Schema"""

    ai_task: str
    explanation: str = Field(description="Explanation for having the given ai task.")


class AITaskList(BaseModel):
    """AITaskList Response Schema"""

    ai_tasks: List[AITask]


class DomainType(BaseModel):
    """Domain Response Schema"""

    answer: Literal[
        "Customer service/support",
        "Technical",
        "Information retrieval",
        "Strategy",
        "Code/software engineering",
        "Communications",
        "IT/business automation",
        "Writing assistant",
        "Financial",
        "Talent and Organization including HR",
        "Product",
        "Marketing",
        "Cybersecurity",
        "Healthcare",
        "User Research",
        "Sales",
        "Risk and Compliance",
        "Design",
        "Other",
    ] = Field(description="Domain type of the usecase.")
    explanation: str = Field(
        description="Explanation for having the given domain type."
    )


RISK_CATEGORY_SCHEMA = {
    "type": "object",
    "properties": {
        "Description": {"type": "string"},
        "Classification": {
            "type": "string",
            "enum": [
                EuAiRiskCategory.EXCLUDED.value,
                EuAiRiskCategory.PROHIBITED.value,
                EuAiRiskCategory.HIGH_RISK_EXCEPTION.value,
                EuAiRiskCategory.HIGH_RISK.value,
                EuAiRiskCategory.LIMITED_OR_LOW_RISK.value,
            ],
        },
        "AIActText": {"type": "string"},
        "Reasoning": {"type": "string"},
    },
    "required": [
        "Description",
        "Classification",
        "AIActText",
        "Reasoning",
    ],
}
