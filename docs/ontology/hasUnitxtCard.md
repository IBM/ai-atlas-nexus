---
search:
  boost: 5.0
---

# Slot: hasUnitxtCard

_A relationship to a Unitxt card defining the risk evaluation_

<div data-search-exclude markdown="1">

URI: [nexus:hasUnitxtCard](https://w3id.org/ai-atlas-nexus/hasUnitxtCard)

<!-- no inheritance hierarchy -->

## Applicable Classes

| Name                              | Description                                       | Modifies Slot |
| --------------------------------- | ------------------------------------------------- | ------------- |
| [AiEval](AiEval.md)               | An AI Evaluation, e                               | no            |
| [Question](Question.md)           | An evaluation where a question has to be answered | no            |
| [Questionnaire](Questionnaire.md) | A questionnaire groups questions                  | no            |

## Properties

### Type and Range

| Property  | Value                                                                |
| --------- | -------------------------------------------------------------------- |
| Range     | [Uri](Uri.md)                                                        |
| Domain Of | [AiEval](AiEval.md)                                                  |
| Slot URI  | [nexus:hasUnitxtCard](https://w3id.org/ai-atlas-nexus/hasUnitxtCard) |

### Cardinality and Requirements

| Property    | Value |
| ----------- | ----- |
| Multivalued | Yes   |

## Identifier and Mapping Information

### Schema Source

- from schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology

## Mappings

| Mapping Type | Mapped Value        |
| ------------ | ------------------- |
| self         | nexus:hasUnitxtCard |
| native       | nexus:hasUnitxtCard |

## LinkML Source

<details>
```yaml
name: hasUnitxtCard
description: A relationship to a Unitxt card defining the risk evaluation
from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
rank: 1000
slot_uri: nexus:hasUnitxtCard
domain_of:
- AiEval
range: uri
multivalued: true
inlined: false

```
</details></div>
```
