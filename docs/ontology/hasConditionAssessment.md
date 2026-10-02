---
search:
  boost: 5.0
---

# Slot: hasConditionAssessment

_The per-condition answers of a completed checklist._

<div data-search-exclude markdown="1">

URI: [nexus:hasConditionAssessment](https://w3id.org/ai-atlas-nexus/hasConditionAssessment)

<!-- no inheritance hierarchy -->

## Applicable Classes

| Name                                                              | Description                                                                      | Modifies Slot |
| ----------------------------------------------------------------- | -------------------------------------------------------------------------------- | ------------- |
| [EvaluationStandardConformance](EvaluationStandardConformance.md) | A completed checklist reporting how an engagement addressed the conditions of... | no            |

## Properties

### Type and Range

| Property  | Value                                                                                  |
| --------- | -------------------------------------------------------------------------------------- |
| Range     | [ConditionAssessment](ConditionAssessment.md)                                          |
| Domain Of | [EvaluationStandardConformance](EvaluationStandardConformance.md)                      |
| Slot URI  | [nexus:hasConditionAssessment](https://w3id.org/ai-atlas-nexus/hasConditionAssessment) |

### Cardinality and Requirements

| Property    | Value |
| ----------- | ----- |
| Multivalued | Yes   |

## Identifier and Mapping Information

### Schema Source

- from schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology

## Mappings

| Mapping Type | Mapped Value                 |
| ------------ | ---------------------------- |
| self         | nexus:hasConditionAssessment |
| native       | nexus:hasConditionAssessment |

## LinkML Source

<details>
```yaml
name: hasConditionAssessment
description: The per-condition answers of a completed checklist.
from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
rank: 1000
slot_uri: nexus:hasConditionAssessment
domain_of:
- EvaluationStandardConformance
range: ConditionAssessment
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>
```
