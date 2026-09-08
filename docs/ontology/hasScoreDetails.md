---
search:
  boost: 5.0
---

# Slot: hasScoreDetails

_Score details_

<div data-search-exclude markdown="1">

URI: [nexus:hasScoreDetails](https://w3id.org/ai-atlas-nexus/hasScoreDetails)

<!-- no inheritance hierarchy -->

## Applicable Classes

| Name                                                | Description                       | Modifies Slot |
| --------------------------------------------------- | --------------------------------- | ------------- |
| [EvaluationResultRecord](EvaluationResultRecord.md) | A single evaluation result record | no            |

## Properties

### Type and Range

| Property  | Value                                               |
| --------- | --------------------------------------------------- |
| Range     | [ScoreDetails](ScoreDetails.md)                     |
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
| self         | nexus:hasScoreDetails |
| native       | nexus:hasScoreDetails |

## LinkML Source

<details>
```yaml
name: hasScoreDetails
description: Score details
from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
rank: 1000
domain: EvaluationResultRecord
domain_of:
- EvaluationResultRecord
range: ScoreDetails
inlined: true

```
</details></div>
```
