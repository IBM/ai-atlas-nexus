# Slot: hasScoreDetails

_Score details_

URI: [nexus:hasScoreDetails](https://ibm.github.io/ai-atlas-nexus/ontology/hasScoreDetails)
Alias: hasScoreDetails

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

- from schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology

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
from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
rank: 1000
domain: EvaluationResultRecord
alias: hasScoreDetails
domain_of:
- EvaluationResultRecord
range: ScoreDetails
inlined: true

```
</details>
```
