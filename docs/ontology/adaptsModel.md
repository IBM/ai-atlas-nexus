---
search:
  boost: 5.0
---

# Slot: adaptsModel

_The LargeLanguageModel being adapted_

<div data-search-exclude markdown="1">

URI: [nexus:adaptsModel](https://w3id.org/ai-atlas-nexus/adaptsModel)

<!-- no inheritance hierarchy -->

## Applicable Classes

| Name                  | Description                                                                      | Modifies Slot |
| --------------------- | -------------------------------------------------------------------------------- | ------------- |
| [Adapter](Adapter.md) | Adapter-based methods add extra trainable parameters after the attention and ... | no            |

## Properties

### Type and Range

| Property  | Value                                       |
| --------- | ------------------------------------------- |
| Range     | [LargeLanguageModel](LargeLanguageModel.md) |
| Domain Of | [Adapter](Adapter.md)                       |

### Cardinality and Requirements

| Property    | Value |
| ----------- | ----- |
| Multivalued | Yes   |

## Identifier and Mapping Information

### Schema Source

- from schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology

## Mappings

| Mapping Type | Mapped Value      |
| ------------ | ----------------- |
| self         | nexus:adaptsModel |
| native       | nexus:adaptsModel |

## LinkML Source

<details>
```yaml
name: adaptsModel
description: The LargeLanguageModel being adapted
from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
rank: 1000
domain_of:
- Adapter
range: LargeLanguageModel
multivalued: true

```
</details></div>
```
