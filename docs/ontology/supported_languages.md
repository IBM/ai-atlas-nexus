---
search:
  boost: 5.0
---

# Slot: supported_languages

_A list of languages, expressed as ISO two letter codes. For example, 'jp, fr, en, de'_

<div data-search-exclude markdown="1">

URI: [nexus:supported_languages](https://w3id.org/ai-atlas-nexus/supported_languages)
Alias: supported_languages

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

| Property    | Value |
| ----------- | ----- |
| Multivalued | Yes   |

## Identifier and Mapping Information

### Schema Source

- from schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology

## Mappings

| Mapping Type | Mapped Value              |
| ------------ | ------------------------- |
| self         | nexus:supported_languages |
| native       | nexus:supported_languages |

## LinkML Source

<details>
```yaml
name: supported_languages
description: A list of languages, expressed as ISO two letter codes. For example,
  'jp, fr, en, de'
from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
rank: 1000
alias: supported_languages
domain_of:
- LargeLanguageModel
range: string
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>
```
