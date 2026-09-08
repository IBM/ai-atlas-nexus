---
search:
  boost: 5.0
---

# Slot: concern

_Some explanation about the concern related to an AI risk_

<div data-search-exclude markdown="1">

URI: [nexus:concern](https://w3id.org/ai-atlas-nexus/concern)

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

| Property | Value |
| -------- | ----- |

### Slot Characteristics

| Property | Value           |
| -------- | --------------- |
| Owner    | [Risk](Risk.md) |

## Identifier and Mapping Information

### Schema Source

- from schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology

## Mappings

| Mapping Type | Mapped Value  |
| ------------ | ------------- |
| self         | nexus:concern |
| native       | nexus:concern |

## LinkML Source

<details>
```yaml
name: concern
description: Some explanation about the concern related to an AI risk
from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
rank: 1000
owner: Risk
domain_of:
- Risk
range: string

```
</details></div>
```
