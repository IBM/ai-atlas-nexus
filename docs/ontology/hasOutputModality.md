---
search:
  boost: 5.0
---

# Slot: hasOutputModality

_A relationship indicating the output modalities supported by an AI component. Examples include text, image, video._

<div data-search-exclude markdown="1">

URI: [nexus:hasOutputModality](https://w3id.org/ai-atlas-nexus/hasOutputModality)

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
| Range     | [Modality](Modality.md)                     |
| Domain Of | [LargeLanguageModel](LargeLanguageModel.md) |

### Cardinality and Requirements

| Property    | Value |
| ----------- | ----- |
| Multivalued | Yes   |

## Identifier and Mapping Information

### Schema Source

- from schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology

## Mappings

| Mapping Type | Mapped Value            |
| ------------ | ----------------------- |
| self         | nexus:hasOutputModality |
| native       | nexus:hasOutputModality |

## LinkML Source

<details>
```yaml
name: hasOutputModality
description: A relationship indicating the output modalities supported by an AI component.
  Examples include text, image, video.
from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
rank: 1000
domain_of:
- LargeLanguageModel
range: Modality
multivalued: true
inlined: false

```
</details></div>
```
