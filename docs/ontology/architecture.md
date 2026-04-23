# Slot: architecture

_A description of the architecture of an AI such as 'Decoder-only'._

URI: [nexus:architecture](https://ibm.github.io/ai-atlas-nexus/ontology/architecture)
Alias: architecture

<!-- no inheritance hierarchy -->

## Applicable Classes

| Name                                        | Description                                                                      | Modifies Slot |
| ------------------------------------------- | -------------------------------------------------------------------------------- | ------------- |
| [Adapter](Adapter.md)                       | Adapter-based methods add extra trainable parameters after the attention and ... | no            |
| [LargeLanguageModel](LargeLanguageModel.md) | A large language model (LLM) is an AI model which supports a range of languag... | no            |
| [AiModel](AiModel.md)                       | A base AI Model class                                                            | no            |

## Properties

### Type and Range

| Property  | Value                 |
| --------- | --------------------- |
| Range     | [String](String.md)   |
| Domain Of | [AiModel](AiModel.md) |

### Cardinality and Requirements

| Property | Value |
| -------- | ----- |

## Identifier and Mapping Information

### Schema Source

- from schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology

## Mappings

| Mapping Type | Mapped Value       |
| ------------ | ------------------ |
| self         | nexus:architecture |
| native       | nexus:architecture |

## LinkML Source

<details>
```yaml
name: architecture
description: A description of the architecture of an AI such as 'Decoder-only'.
from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
rank: 1000
alias: architecture
domain_of:
- AiModel
range: string

```
</details>
```
