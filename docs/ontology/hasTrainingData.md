---
search:
  boost: 5.0
---

# Slot: hasTrainingData

_A relationship indicating the datasets an AI model was trained on._

<div data-search-exclude markdown="1">

URI: [airo:hasTrainingData](https://w3id.org/airo#hasTrainingData)

<!-- no inheritance hierarchy -->

## Applicable Classes

| Name                                        | Description                                                                      | Modifies Slot |
| ------------------------------------------- | -------------------------------------------------------------------------------- | ------------- |
| [LargeLanguageModel](LargeLanguageModel.md) | A large language model (LLM) is an AI model which supports a range of languag... | no            |
| [Adapter](Adapter.md)                       | Adapter-based methods add extra trainable parameters after the attention and ... | no            |

## Properties

### Type and Range

| Property  | Value                                                         |
| --------- | ------------------------------------------------------------- |
| Range     | [Dataset](Dataset.md)                                         |
| Domain Of | [LargeLanguageModel](LargeLanguageModel.md)                   |
| Slot URI  | [airo:hasTrainingData](https://w3id.org/airo#hasTrainingData) |

### Cardinality and Requirements

| Property    | Value |
| ----------- | ----- |
| Multivalued | Yes   |

## Identifier and Mapping Information

### Schema Source

- from schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology

## Mappings

| Mapping Type | Mapped Value          |
| ------------ | --------------------- |
| self         | airo:hasTrainingData  |
| native       | nexus:hasTrainingData |

## LinkML Source

<details>
```yaml
name: hasTrainingData
description: A relationship indicating the datasets an AI model was trained on.
from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
rank: 1000
slot_uri: airo:hasTrainingData
domain_of:
- LargeLanguageModel
range: Dataset
multivalued: true
inlined: false

```
</details></div>
```
