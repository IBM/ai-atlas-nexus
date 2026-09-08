---
search:
  boost: 5.0
---

# Slot: carbon_emitted

_The number of tons of carbon dioxide equivalent that are emitted during training_

<div data-search-exclude markdown="1">

URI: [nexus:carbon_emitted](https://w3id.org/ai-atlas-nexus/carbon_emitted)

<!-- no inheritance hierarchy -->

## Applicable Classes

| Name                                        | Description                                                                      | Modifies Slot |
| ------------------------------------------- | -------------------------------------------------------------------------------- | ------------- |
| [AiModel](AiModel.md)                       | A base AI Model class                                                            | no            |
| [LargeLanguageModel](LargeLanguageModel.md) | A large language model (LLM) is an AI model which supports a range of languag... | no            |
| [Adapter](Adapter.md)                       | Adapter-based methods add extra trainable parameters after the attention and ... | no            |

## Properties

### Type and Range

| Property  | Value                 |
| --------- | --------------------- |
| Range     | [Float](Float.md)     |
| Domain Of | [AiModel](AiModel.md) |

### Cardinality and Requirements

| Property | Value |
| -------- | ----- |

### Value Constraints

| Property      | Value |
| ------------- | ----- |
| Minimum Value | 0     |

<details>
<summary>Additional Constraints</summary>
**Unit:**

| Property         | Value                  |
| ---------------- | ---------------------- |
| symbol           | t CO2-eq               |
| descriptive_name | tons of CO2 equivalent |

</details>

## Identifier and Mapping Information

### Schema Source

- from schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology

## Mappings

| Mapping Type | Mapped Value         |
| ------------ | -------------------- |
| self         | nexus:carbon_emitted |
| native       | nexus:carbon_emitted |

## LinkML Source

<details>
```yaml
name: carbon_emitted
description: The number of tons of carbon dioxide equivalent that are emitted during
  training
from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
rank: 1000
domain_of:
- AiModel
range: float
minimum_value: 0
unit:
  symbol: t CO2-eq
  descriptive_name: tons of CO2 equivalent

```
</details></div>
```
