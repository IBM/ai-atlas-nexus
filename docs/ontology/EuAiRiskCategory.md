# Enum: EuAiRiskCategory

URI: [nexus:EuAiRiskCategory](https://ibm.github.io/ai-atlas-nexus/ontology/EuAiRiskCategory)

## Permissible Values

| Value               | Meaning | Description         |
| ------------------- | ------- | ------------------- |
| EXCLUDED            | None    | Excluded            |
| PROHIBITED          | None    | Prohibited          |
| HIGH_RISK_EXCEPTION | None    | High-Risk Exception |
| HIGH_RISK           | None    | High Risk           |
| LIMITED_OR_LOW_RISK | None    | Limited or Low Risk |

## Slots

| Name                                      | Description                                                   |
| ----------------------------------------- | ------------------------------------------------------------- |
| [hasEuRiskCategory](hasEuRiskCategory.md) | The risk category of an AI system as defined by the EU AI Act |

## Identifier and Mapping Information

### Schema Source

- from schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology

## LinkML Source

<details>
```yaml
name: EuAiRiskCategory
from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
rank: 1000
permissible_values:
  EXCLUDED:
    text: EXCLUDED
    description: Excluded
  PROHIBITED:
    text: PROHIBITED
    description: Prohibited
  HIGH_RISK_EXCEPTION:
    text: HIGH_RISK_EXCEPTION
    description: High-Risk Exception
  HIGH_RISK:
    text: HIGH_RISK
    description: High Risk
  LIMITED_OR_LOW_RISK:
    text: LIMITED_OR_LOW_RISK
    description: Limited or Low Risk

```
</details>
```
