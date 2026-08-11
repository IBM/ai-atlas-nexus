---
search:
  boost: 5.0
---

# Slot: hasModelCard

_A relationship to model card references._

<div data-search-exclude markdown="1">

URI: [nexus:hasModelCard](https://w3id.org/ai-atlas-nexus/hasModelCard)
Alias: hasModelCard

<!-- no inheritance hierarchy -->

## Applicable Classes

| Name                                        | Description                                                                      | Modifies Slot |
| ------------------------------------------- | -------------------------------------------------------------------------------- | ------------- |
| [Adapter](Adapter.md)                       | Adapter-based methods add extra trainable parameters after the attention and ... | no            |
| [AiModel](AiModel.md)                       | A base AI Model class                                                            | no            |
| [AiAgent](AiAgent.md)                       | An artificial intelligence (AI) agent refers to a system or program that is c... | no            |
| [LargeLanguageModel](LargeLanguageModel.md) | A large language model (LLM) is an AI model which supports a range of languag... | no            |
| [AiSystem](AiSystem.md)                     | A compound AI System composed of one or more AI capablities                      | no            |
| [BaseAi](BaseAi.md)                         | Any type of AI, be it a LLM, RL agent, SVM, etc                                  | no            |

## Properties

### Type and Range

| Property  | Value               |
| --------- | ------------------- |
| Range     | [String](String.md) |
| Domain Of | [BaseAi](BaseAi.md) |

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
| self         | nexus:hasModelCard |
| native       | nexus:hasModelCard |

## LinkML Source

<details>
```yaml
name: hasModelCard
description: A relationship to model card references.
from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
rank: 1000
alias: hasModelCard
domain_of:
- BaseAi
range: string
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>
```
