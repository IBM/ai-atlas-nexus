---
search:
  boost: 5.0
---

# Slot: implementsCapability

_Indicates that this entity implements a specific capability_

<div data-search-exclude markdown="1">

URI: [nexus:implementsCapability](https://w3id.org/ai-atlas-nexus/implementsCapability)

<!-- no inheritance hierarchy -->

## Applicable Classes

| Name                            | Description                                                                      | Modifies Slot |
| ------------------------------- | -------------------------------------------------------------------------------- | ------------- |
| [Adapter](Adapter.md)           | Adapter-based methods add extra trainable parameters after the attention and ... | yes           |
| [LLMIntrinsic](LLMIntrinsic.md) | A capability that can be invoked through a well-defined API that is reasonabl... | yes           |

## Properties

### Type and Range

| Property  | Value                                                  |
| --------- | ------------------------------------------------------ |
| Range     | [Any](Any.md)                                          |
| Domain    | [Any](Any.md)                                          |
| Domain Of | [Adapter](Adapter.md), [LLMIntrinsic](LLMIntrinsic.md) |

### Cardinality and Requirements

| Property    | Value |
| ----------- | ----- |
| Multivalued | Yes   |

## Identifier and Mapping Information

### Schema Source

- from schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology

## Mappings

| Mapping Type | Mapped Value               |
| ------------ | -------------------------- |
| self         | nexus:implementsCapability |
| native       | nexus:implementsCapability |

## LinkML Source

<details>
```yaml
name: implementsCapability
description: Indicates that this entity implements a specific capability
from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
rank: 1000
domain: Any
domain_of:
- Adapter
- LLMIntrinsic
range: Any
multivalued: true
inlined: false

```
</details></div>
```
