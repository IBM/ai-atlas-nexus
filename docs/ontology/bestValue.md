---
search:
  boost: 5.0
---

# Slot: bestValue

_Annotation of the best possible result of the evaluation_

<div data-search-exclude markdown="1">

URI: [nexus:bestValue](https://w3id.org/ai-atlas-nexus/bestValue)
Alias: bestValue

<!-- no inheritance hierarchy -->

## Applicable Classes

| Name                              | Description                                       | Modifies Slot |
| --------------------------------- | ------------------------------------------------- | ------------- |
| [AiEval](AiEval.md)               | An AI Evaluation, e                               | no            |
| [Question](Question.md)           | An evaluation where a question has to be answered | no            |
| [Questionnaire](Questionnaire.md) | A questionnaire groups questions                  | no            |

## Properties

### Type and Range

| Property  | Value               |
| --------- | ------------------- |
| Range     | [String](String.md) |
| Domain Of | [AiEval](AiEval.md) |

### Cardinality and Requirements

| Property | Value |
| -------- | ----- |

## Identifier and Mapping Information

### Schema Source

- from schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology

## Mappings

| Mapping Type | Mapped Value    |
| ------------ | --------------- |
| self         | nexus:bestValue |
| native       | nexus:bestValue |

## LinkML Source

<details>
```yaml
name: bestValue
description: Annotation of the best possible result of the evaluation
from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
rank: 1000
alias: bestValue
domain_of:
- AiEval
range: string

```
</details></div>
```
