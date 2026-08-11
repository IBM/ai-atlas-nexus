---
search:
  boost: 5.0
---

# Slot: gpu_hours

_GPU consumption in terms of hours_

<div data-search-exclude markdown="1">

URI: [nexus:gpu_hours](https://w3id.org/ai-atlas-nexus/gpu_hours)
Alias: gpu_hours

<!-- no inheritance hierarchy -->

## Applicable Classes

| Name                                        | Description                                                                      | Modifies Slot |
| ------------------------------------------- | -------------------------------------------------------------------------------- | ------------- |
| [LargeLanguageModel](LargeLanguageModel.md) | A large language model (LLM) is an AI model which supports a range of languag... | no            |
| [Adapter](Adapter.md)                       | Adapter-based methods add extra trainable parameters after the attention and ... | no            |
| [AiModel](AiModel.md)                       | A base AI Model class                                                            | no            |

## Properties

### Type and Range

| Property  | Value                 |
| --------- | --------------------- |
| Range     | [Integer](Integer.md) |
| Domain Of | [AiModel](AiModel.md) |

### Cardinality and Requirements

| Property | Value |
| -------- | ----- |

### Value Constraints

| Property      | Value |
| ------------- | ----- |
| Minimum Value | 0     |

## Identifier and Mapping Information

### Schema Source

- from schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology

## Mappings

| Mapping Type | Mapped Value    |
| ------------ | --------------- |
| self         | nexus:gpu_hours |
| native       | nexus:gpu_hours |

## LinkML Source

<details>
```yaml
name: gpu_hours
description: GPU consumption in terms of hours
from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
rank: 1000
alias: gpu_hours
domain_of:
- AiModel
range: integer
minimum_value: 0

```
</details></div>
```
