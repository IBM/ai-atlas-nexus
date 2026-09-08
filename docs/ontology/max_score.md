---
search:
  boost: 5.0
---

# Slot: max_score

_Maximum possible score_

<div data-search-exclude markdown="1">

URI: [nexus:max_score](https://w3id.org/ai-atlas-nexus/max_score)

<!-- no inheritance hierarchy -->

## Applicable Classes

| Name                            | Description                          | Modifies Slot |
| ------------------------------- | ------------------------------------ | ------------- |
| [MetricConfig](MetricConfig.md) | Configuration for evaluation metrics | no            |

## Properties

### Type and Range

| Property  | Value                           |
| --------- | ------------------------------- |
| Range     | [Float](Float.md)               |
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

| Mapping Type | Mapped Value    |
| ------------ | --------------- |
| self         | nexus:max_score |
| native       | nexus:max_score |

## LinkML Source

<details>
```yaml
name: max_score
description: Maximum possible score
from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
rank: 1000
owner: MetricConfig
domain_of:
- MetricConfig
range: float

```
</details></div>
```
