---
search:
  boost: 5.0
---

# Slot: lower_is_better

_Whether lower scores are better_

<div data-search-exclude markdown="1">

URI: [nexus:lower_is_better](https://w3id.org/ai-atlas-nexus/lower_is_better)

<!-- no inheritance hierarchy -->

## Applicable Classes

| Name                            | Description                          | Modifies Slot |
| ------------------------------- | ------------------------------------ | ------------- |
| [MetricConfig](MetricConfig.md) | Configuration for evaluation metrics | no            |

## Properties

### Type and Range

| Property  | Value                           |
| --------- | ------------------------------- |
| Range     | [Boolean](Boolean.md)           |
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

| Mapping Type | Mapped Value          |
| ------------ | --------------------- |
| self         | nexus:lower_is_better |
| native       | nexus:lower_is_better |

## LinkML Source

<details>
```yaml
name: lower_is_better
description: Whether lower scores are better
from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
rank: 1000
owner: MetricConfig
domain_of:
- MetricConfig
range: boolean

```
</details></div>
```
