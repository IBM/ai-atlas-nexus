---
search:
  boost: 5.0
---

# Slot: phase

_Annotation whether an AI risk shows specifically during the training-tuning or inference phase._

<div data-search-exclude markdown="1">

URI: [nexus:phase](https://w3id.org/ai-atlas-nexus/phase)

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

| Mapping Type | Mapped Value |
| ------------ | ------------ |
| self         | nexus:phase  |
| native       | nexus:phase  |

## LinkML Source

<details>
```yaml
name: phase
description: Annotation whether an AI risk shows specifically during the training-tuning
  or inference phase.
from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
rank: 1000
owner: Risk
domain_of:
- Risk
range: string

```
</details></div>
```
