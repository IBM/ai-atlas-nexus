---
search:
  boost: 5.0
---

# Slot: hasCapability

_Indicates the technical capabilities this entry possesses._

\_\_

<div data-search-exclude markdown="1">

URI: [tech:hasCapability](https://w3id.org/dpv/tech#hasCapability)

<!-- no inheritance hierarchy -->

## Applicable Classes

| Name                            | Description                                                                      | Modifies Slot |
| ------------------------------- | -------------------------------------------------------------------------------- | ------------- |
| [AiSystem](AiSystem.md)         | A compound AI System composed of one or more AI capablities                      | yes           |
| [Adapter](Adapter.md)           | Adapter-based methods add extra trainable parameters after the attention and ... | no            |
| [LLMIntrinsic](LLMIntrinsic.md) | A capability that can be invoked through a well-defined API that is reasonabl... | no            |
| [AiAgent](AiAgent.md)           | An artificial intelligence (AI) agent refers to a system or program that is c... | no            |

## Properties

### Type and Range

| Property  | Value                                                                           |
| --------- | ------------------------------------------------------------------------------- |
| Range     | [Capability](Capability.md)                                                     |
| Domain Of | [AiSystem](AiSystem.md), [Adapter](Adapter.md), [LLMIntrinsic](LLMIntrinsic.md) |
| Slot URI  | [tech:hasCapability](https://w3id.org/dpv/tech#hasCapability)                   |

### Cardinality and Requirements

| Property    | Value |
| ----------- | ----- |
| Multivalued | Yes   |

## Identifier and Mapping Information

### Schema Source

- from schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology

## Mappings

| Mapping Type | Mapped Value        |
| ------------ | ------------------- |
| self         | tech:hasCapability  |
| native       | nexus:hasCapability |

## LinkML Source

<details>
```yaml
name: hasCapability
description: 'Indicates the technical capabilities this entry possesses.

'
from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
rank: 1000
slot_uri: tech:hasCapability
domain_of:

- AiSystem
- Adapter
- LLMIntrinsic
  range: Capability
  multivalued: true
  inlined: false

```
</details></div>
```
