---
search:
  boost: 5.0
---

# Slot: score_type

_Type of score (e.g., continuous)_

<div data-search-exclude markdown="1">

URI: [nexus:score_type](https://w3id.org/ai-atlas-nexus/score_type)

<!-- no inheritance hierarchy -->

## Applicable Classes

| Name                            | Description                          | Modifies Slot |
| ------------------------------- | ------------------------------------ | ------------- |
| [MetricConfig](MetricConfig.md) | Configuration for evaluation metrics | no            |

## Properties

### Type and Range

| Property  | Value                           |
| --------- | ------------------------------- |
| Range     | [String](String.md)             |
| Domain Of | [MetricConfig](MetricConfig.md) |

### Cardinality and Requirements

| Property | Value |
| -------- | ----- |

### Slot Characteristics

| Property | Value                           |
| -------- | ------------------------------- |
| Owner    | [MetricConfig](MetricConfig.md) |

## Identifier and Mapping Information

### Schema Source

- from schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology

## Mappings

| Mapping Type | Mapped Value     |
| ------------ | ---------------- |
| self         | nexus:score_type |
| native       | nexus:score_type |

## LinkML Source

<details>
```yaml
name: score_type
description: Type of score (e.g., continuous)
from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
rank: 1000
owner: MetricConfig
domain_of:
- MetricConfig
range: string

```
</details></div>
```
