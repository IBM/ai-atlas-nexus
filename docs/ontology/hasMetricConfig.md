---
search:
  boost: 5.0
---

# Slot: hasMetricConfig

_Metric configuration_

<div data-search-exclude markdown="1">

URI: [nexus:hasMetricConfig](https://w3id.org/ai-atlas-nexus/hasMetricConfig)

<!-- no inheritance hierarchy -->

## Applicable Classes

| Name                                                | Description                       | Modifies Slot |
| --------------------------------------------------- | --------------------------------- | ------------- |
| [EvaluationResultRecord](EvaluationResultRecord.md) | A single evaluation result record | no            |

## Properties

### Type and Range

| Property  | Value                                               |
| --------- | --------------------------------------------------- |
| Range     | [MetricConfig](MetricConfig.md)                     |
| Domain    | [EvaluationResultRecord](EvaluationResultRecord.md) |
| Domain Of | [EvaluationResultRecord](EvaluationResultRecord.md) |

### Cardinality and Requirements

| Property | Value |
| -------- | ----- |

## Identifier and Mapping Information

### Schema Source

- from schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology

## Mappings

| Mapping Type | Mapped Value          |
| ------------ | --------------------- |
| self         | nexus:hasMetricConfig |
| native       | nexus:hasMetricConfig |

## LinkML Source

<details>
```yaml
name: hasMetricConfig
description: Metric configuration
from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
rank: 1000
domain: EvaluationResultRecord
domain_of:
- EvaluationResultRecord
range: MetricConfig
inlined: true

```
</details></div>
```
