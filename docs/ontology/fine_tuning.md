---
search:
  boost: 5.0
---

# Slot: fine_tuning

_A description of the fine-tuning mechanism(s) applied to a model._

<div data-search-exclude markdown="1">

URI: [nexus:fine_tuning](https://w3id.org/ai-atlas-nexus/fine_tuning)

<!-- no inheritance hierarchy -->

## Applicable Classes

| Name                                        | Description                                                                      | Modifies Slot |
| ------------------------------------------- | -------------------------------------------------------------------------------- | ------------- |
| [LargeLanguageModel](LargeLanguageModel.md) | A large language model (LLM) is an AI model which supports a range of languag... | no            |
| [Adapter](Adapter.md)                       | Adapter-based methods add extra trainable parameters after the attention and ... | no            |

## Properties

### Type and Range

| Property  | Value                                       |
| --------- | ------------------------------------------- |
| Range     | [String](String.md)                         |
| Domain Of | [LargeLanguageModel](LargeLanguageModel.md) |

### Cardinality and Requirements

| Property | Value |
| -------- | ----- |

## Identifier and Mapping Information

### Schema Source

- from schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology

## Mappings

| Mapping Type | Mapped Value      |
| ------------ | ----------------- |
| self         | nexus:fine_tuning |
| native       | nexus:fine_tuning |

## LinkML Source

<details>
```yaml
name: fine_tuning
description: A description of the fine-tuning mechanism(s) applied to a model.
from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
rank: 1000
domain_of:
- LargeLanguageModel
range: string

```
</details></div>
```
