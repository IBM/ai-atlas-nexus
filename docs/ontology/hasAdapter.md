---
search:
  boost: 5.0
---

# Slot: hasAdapter

_The Adapter for the intrinsic_

<div data-search-exclude markdown="1">

URI: [nexus:hasAdapter](https://w3id.org/ai-atlas-nexus/hasAdapter)

<!-- no inheritance hierarchy -->

## Applicable Classes

| Name                            | Description                                                                      | Modifies Slot |
| ------------------------------- | -------------------------------------------------------------------------------- | ------------- |
| [LLMIntrinsic](LLMIntrinsic.md) | A capability that can be invoked through a well-defined API that is reasonabl... | no            |

## Properties

### Type and Range

| Property  | Value                           |
| --------- | ------------------------------- |
| Range     | [Adapter](Adapter.md)           |
| Domain    | [LLMIntrinsic](LLMIntrinsic.md) |
| Domain Of | [LLMIntrinsic](LLMIntrinsic.md) |

### Cardinality and Requirements

| Property    | Value |
| ----------- | ----- |
| Multivalued | Yes   |

## Identifier and Mapping Information

### Schema Source

- from schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology

## Mappings

| Mapping Type | Mapped Value     |
| ------------ | ---------------- |
| self         | nexus:hasAdapter |
| native       | nexus:hasAdapter |

## LinkML Source

<details>
```yaml
name: hasAdapter
description: The Adapter for the intrinsic
from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
rank: 1000
domain: LLMIntrinsic
domain_of:
- LLMIntrinsic
range: Adapter
multivalued: true
inlined: false

```
</details></div>
```
