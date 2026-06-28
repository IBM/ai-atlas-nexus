# Slot: hasMetricConfig

_Metric configuration_

URI: [nexus:hasMetricConfig](https://ibm.github.io/ai-atlas-nexus/ontology/hasMetricConfig)
Alias: hasMetricConfig

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

- from schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology

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
from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
rank: 1000
domain: EvaluationResultRecord
alias: hasMetricConfig
domain_of:
- EvaluationResultRecord
range: MetricConfig
inlined: true

```
</details>
```
