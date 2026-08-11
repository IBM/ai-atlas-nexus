---
search:
  boost: 5.0
---

# Slot: isProvidedBy

_A relationship to the Organization instance that provides this instance._

<div data-search-exclude markdown="1">

URI: [schema:provider](http://schema.org/provider)
Alias: isProvidedBy

<!-- no inheritance hierarchy -->

## Applicable Classes

| Name                                        | Description                                                                      | Modifies Slot |
| ------------------------------------------- | -------------------------------------------------------------------------------- | ------------- |
| [Adapter](Adapter.md)                       | Adapter-based methods add extra trainable parameters after the attention and ... | no            |
| [Dataset](Dataset.md)                       | A body of structured information describing some topic(s) of interest            | no            |
| [AiModel](AiModel.md)                       | A base AI Model class                                                            | no            |
| [AiAgent](AiAgent.md)                       | An artificial intelligence (AI) agent refers to a system or program that is c... | yes           |
| [LargeLanguageModel](LargeLanguageModel.md) | A large language model (LLM) is an AI model which supports a range of languag... | no            |
| [AiSystem](AiSystem.md)                     | A compound AI System composed of one or more AI capablities                      | no            |
| [BaseAi](BaseAi.md)                         | Any type of AI, be it a LLM, RL agent, SVM, etc                                  | no            |

## Properties

### Type and Range

| Property  | Value                                         |
| --------- | --------------------------------------------- |
| Range     | [Organization](Organization.md)               |
| Domain Of | [Dataset](Dataset.md), [BaseAi](BaseAi.md)    |
| Slot URI  | [schema:provider](http://schema.org/provider) |

### Cardinality and Requirements

| Property | Value |
| -------- | ----- |

## Identifier and Mapping Information

### Schema Source

- from schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology

## Mappings

| Mapping Type | Mapped Value       |
| ------------ | ------------------ |
| self         | schema:provider    |
| native       | nexus:isProvidedBy |

## LinkML Source

<details>
```yaml
name: isProvidedBy
description: A relationship to the Organization instance that provides this instance.
from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
rank: 1000
slot_uri: schema:provider
alias: isProvidedBy
domain_of:
- Dataset
- BaseAi
range: Organization

```
</details></div>
```
