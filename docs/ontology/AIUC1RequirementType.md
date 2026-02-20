# Enum: AIUC1RequirementType

URI: [nexus:AIUC1RequirementType](https://ibm.github.io/ai-atlas-nexus/ontology/AIUC1RequirementType)

## Permissible Values

| Value        | Meaning | Description  |
| ------------ | ------- | ------------ |
| DETECTIVE    | None    | Detective    |
| PREVENTATIVE | None    | Preventative |

## Slots

| Name                                        | Description                                                        |
| ------------------------------------------- | ------------------------------------------------------------------ |
| [hasRequirementType](hasRequirementType.md) | The requirement type of whether this is preventive, detective, etc |

## Identifier and Mapping Information

### Schema Source

- from schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology

## LinkML Source

<details>
```yaml
name: AIUC1RequirementType
from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
rank: 1000
permissible_values:
  DETECTIVE:
    text: DETECTIVE
    description: Detective
  PREVENTATIVE:
    text: PREVENTATIVE
    description: Preventative

```
</details>
```
