---
search:
  boost: 5.0
---

# Slot: hasAdapterType

_The Adapter type, for example: LORA, ALORA, X-LORA_

<div data-search-exclude markdown="1">

URI: [nexus:hasAdapterType](https://w3id.org/ai-atlas-nexus/hasAdapterType)

<!-- no inheritance hierarchy -->

## Applicable Classes

| Name                  | Description                                                                      | Modifies Slot |
| --------------------- | -------------------------------------------------------------------------------- | ------------- |
| [Adapter](Adapter.md) | Adapter-based methods add extra trainable parameters after the attention and ... | no            |

## Properties

### Type and Range

| Property  | Value                         |
| --------- | ----------------------------- |
| Range     | [AdapterType](AdapterType.md) |
| Domain Of | [Adapter](Adapter.md)         |

### Cardinality and Requirements

| Property    | Value |
| ----------- | ----- |
| Multivalued | Yes   |

## Identifier and Mapping Information

### Schema Source

- from schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology

## Mappings

| Mapping Type | Mapped Value         |
| ------------ | -------------------- |
| self         | nexus:hasAdapterType |
| native       | nexus:hasAdapterType |

## LinkML Source

<details>
```yaml
name: hasAdapterType
description: 'The Adapter type, for example: LORA, ALORA, X-LORA'
from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
rank: 1000
domain_of:
- Adapter
range: AdapterType
multivalued: true

```
</details></div>
```
