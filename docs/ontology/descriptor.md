---
search:
  boost: 5.0
---

# Slot: descriptor

_Annotates whether an AI risk is a traditional risk, specific to or amplified by AI._

<div data-search-exclude markdown="1">

URI: [nexus:descriptor](https://w3id.org/ai-atlas-nexus/descriptor)

<!-- no inheritance hierarchy -->

## Applicable Classes

| Name            | Description                                                                      | Modifies Slot |
| --------------- | -------------------------------------------------------------------------------- | ------------- |
| [Risk](Risk.md) | The state of uncertainty associated with an AI system, that has the potential... | no            |

## Properties

### Type and Range

| Property  | Value               |
| --------- | ------------------- |
| Range     | [String](String.md) |
| Domain Of | [Risk](Risk.md)     |

### Cardinality and Requirements

| Property    | Value |
| ----------- | ----- |
| Multivalued | Yes   |

### Slot Characteristics

| Property | Value           |
| -------- | --------------- |
| Owner    | [Risk](Risk.md) |

## Identifier and Mapping Information

### Schema Source

- from schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology

## Mappings

| Mapping Type | Mapped Value     |
| ------------ | ---------------- |
| self         | nexus:descriptor |
| native       | nexus:descriptor |

## LinkML Source

<details>
```yaml
name: descriptor
description: Annotates whether an AI risk is a traditional risk, specific to or amplified
  by AI.
from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
rank: 1000
owner: Risk
domain_of:
- Risk
range: string
multivalued: true

```
</details></div>
```
