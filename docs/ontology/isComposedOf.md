---
search:
  boost: 5.0
---

# Slot: isComposedOf

_Relationship indicating the some entity is composed of other entities (including some of the same type)._

<div data-search-exclude markdown="1">

URI: [nexus:isComposedOf](https://w3id.org/ai-atlas-nexus/isComposedOf)
Alias: isComposedOf

<!-- no inheritance hierarchy -->

## Applicable Classes

| Name                              | Description                                                                      | Modifies Slot |
| --------------------------------- | -------------------------------------------------------------------------------- | ------------- |
| [Questionnaire](Questionnaire.md) | A questionnaire groups questions                                                 | yes           |
| [AiSystem](AiSystem.md)           | A compound AI System composed of one or more AI capablities                      | yes           |
| [AiEval](AiEval.md)               | An AI Evaluation, e                                                              | yes           |
| [AiAgent](AiAgent.md)             | An artificial intelligence (AI) agent refers to a system or program that is c... | no            |
| [Question](Question.md)           | An evaluation where a question has to be answered                                | no            |

## Properties

### Type and Range

| Property  | Value                                        |
| --------- | -------------------------------------------- |
| Range     | [String](String.md)                          |
| Domain Of | [AiSystem](AiSystem.md), [AiEval](AiEval.md) |

### Cardinality and Requirements

| Property    | Value |
| ----------- | ----- |
| Multivalued | Yes   |

## Identifier and Mapping Information

### Schema Source

- from schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology

## Mappings

| Mapping Type | Mapped Value       |
| ------------ | ------------------ |
| self         | nexus:isComposedOf |
| native       | nexus:isComposedOf |

## LinkML Source

<details>
```yaml
name: isComposedOf
description: Relationship indicating the some entity is composed of other entities
  (including some of the same type).
from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
rank: 1000
alias: isComposedOf
domain_of:
- AiSystem
- AiEval
range: string
multivalued: true
inlined: false

```
</details></div>
```
