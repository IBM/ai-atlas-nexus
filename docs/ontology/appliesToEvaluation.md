---
search:
  boost: 5.0
---

# Slot: appliesToEvaluation

_The evaluations of the engagement that this answer is specific to. When absent, the answer applies to the engagement as a whole._

<div data-search-exclude markdown="1">

URI: [nexus:appliesToEvaluation](https://w3id.org/ai-atlas-nexus/appliesToEvaluation)

<!-- no inheritance hierarchy -->

## Applicable Classes

| Name                                          | Description                                                                      | Modifies Slot |
| --------------------------------------------- | -------------------------------------------------------------------------------- | ------------- |
| [ConditionAssessment](ConditionAssessment.md) | One answer of a completed checklist, for one condition of the evaluation stan... | no            |

## Properties

### Type and Range

| Property  | Value                                                                            |
| --------- | -------------------------------------------------------------------------------- |
| Range     | [AiEval](AiEval.md)                                                              |
| Domain Of | [ConditionAssessment](ConditionAssessment.md)                                    |
| Slot URI  | [nexus:appliesToEvaluation](https://w3id.org/ai-atlas-nexus/appliesToEvaluation) |

### Cardinality and Requirements

| Property    | Value |
| ----------- | ----- |
| Multivalued | Yes   |

## Identifier and Mapping Information

### Schema Source

- from schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology

## Mappings

| Mapping Type | Mapped Value              |
| ------------ | ------------------------- |
| self         | nexus:appliesToEvaluation |
| native       | nexus:appliesToEvaluation |

## LinkML Source

<details>
```yaml
name: appliesToEvaluation
description: The evaluations of the engagement that this answer is specific to. When
  absent, the answer applies to the engagement as a whole.
from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
rank: 1000
slot_uri: nexus:appliesToEvaluation
domain_of:
- ConditionAssessment
range: AiEval
multivalued: true
inlined: false

```
</details></div>
```
