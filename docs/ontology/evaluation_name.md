---
search:
  boost: 5.0
---

# Slot: evaluation_name

_Name of the evaluation benchmark_

<div data-search-exclude markdown="1">

URI: [nexus:evaluation_name](https://w3id.org/ai-atlas-nexus/evaluation_name)

<!-- no inheritance hierarchy -->

## Applicable Classes

| Name                                                | Description                       | Modifies Slot |
| --------------------------------------------------- | --------------------------------- | ------------- |
| [EvaluationResultRecord](EvaluationResultRecord.md) | A single evaluation result record | no            |

## Properties

### Type and Range

| Property  | Value                                               |
| --------- | --------------------------------------------------- |
| Range     | [String](String.md)                                 |
| Domain Of | [EvaluationResultRecord](EvaluationResultRecord.md) |

### Cardinality and Requirements

| Property | Value |
| -------- | ----- |

### Slot Characteristics

| Property | Value                                               |
| -------- | --------------------------------------------------- |
| Owner    | [EvaluationResultRecord](EvaluationResultRecord.md) |

## Identifier and Mapping Information

### Schema Source

- from schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology

## Mappings

| Mapping Type | Mapped Value          |
| ------------ | --------------------- |
| self         | nexus:evaluation_name |
| native       | nexus:evaluation_name |

## LinkML Source

<details>
```yaml
name: evaluation_name
description: Name of the evaluation benchmark
from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
rank: 1000
owner: EvaluationResultRecord
domain_of:
- EvaluationResultRecord
range: string

```
</details></div>
```
