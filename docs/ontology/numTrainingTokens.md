---
search:
  boost: 5.0
---

# Slot: numTrainingTokens

_The number of tokens a AI model was trained on._

<div data-search-exclude markdown="1">

URI: [nexus:numTrainingTokens](https://w3id.org/ai-atlas-nexus/numTrainingTokens)

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
| Range     | [Integer](Integer.md)                       |
| Domain Of | [LargeLanguageModel](LargeLanguageModel.md) |

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

| Mapping Type | Mapped Value            |
| ------------ | ----------------------- |
| self         | nexus:numTrainingTokens |
| native       | nexus:numTrainingTokens |

## LinkML Source

<details>
```yaml
name: numTrainingTokens
description: The number of tokens a AI model was trained on.
from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
rank: 1000
domain_of:
- LargeLanguageModel
range: integer
minimum_value: 0

```
</details></div>
```
