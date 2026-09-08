---
search:
  boost: 5.0
---

# Slot: hasSourceData

_Source data information_

<div data-search-exclude markdown="1">

URI: [nexus:hasSourceData](https://w3id.org/ai-atlas-nexus/hasSourceData)

<!-- no inheritance hierarchy -->

## Applicable Classes

| Name                                                | Description                       | Modifies Slot |
| --------------------------------------------------- | --------------------------------- | ------------- |
| [EvaluationResultRecord](EvaluationResultRecord.md) | A single evaluation result record | no            |

## Properties

### Type and Range

| Property  | Value                                               |
| --------- | --------------------------------------------------- |
| Range     | [SourceData](SourceData.md)                         |
| Domain    | [EvaluationResultRecord](EvaluationResultRecord.md) |
| Domain Of | [EvaluationResultRecord](EvaluationResultRecord.md) |

### Cardinality and Requirements

| Property | Value |
| -------- | ----- |

## Identifier and Mapping Information

### Schema Source

- from schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology

## Mappings

| Mapping Type | Mapped Value        |
| ------------ | ------------------- |
| self         | nexus:hasSourceData |
| native       | nexus:hasSourceData |

## LinkML Source

<details>
```yaml
name: hasSourceData
description: Source data information
from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
rank: 1000
domain: EvaluationResultRecord
domain_of:
- EvaluationResultRecord
range: SourceData
inlined: true

```
</details></div>
```
