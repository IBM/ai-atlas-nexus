# Enum: AIUC1ControlApplicationCategory

URI: [nexus:AIUC1ControlApplicationCategory](https://ibm.github.io/ai-atlas-nexus/ontology/AIUC1ControlApplicationCategory)

## Permissible Values

| Value        | Meaning | Description          |
| ------------ | ------- | -------------------- |
| CORE         | None    | Core Control         |
| SUPPLEMENTAL | None    | Supplemental Control |

## Slots

| Name                                              | Description                                                                      |
| ------------------------------------------------- | -------------------------------------------------------------------------------- |
| [hasControlApplication](hasControlApplication.md) | Which of the AIUC-1 ControlApplicationCategory this control activity (rule) b... |

## Identifier and Mapping Information

### Schema Source

- from schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology

## LinkML Source

<details>
```yaml
name: AIUC1ControlApplicationCategory
from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
rank: 1000
permissible_values:
  CORE:
    text: CORE
    description: Core Control
  SUPPLEMENTAL:
    text: SUPPLEMENTAL
    description: Supplemental Control

```
</details>
```
