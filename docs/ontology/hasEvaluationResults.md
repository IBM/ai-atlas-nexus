---
search:
  boost: 5.0
---

# Slot: hasEvaluationResults

_Array of evaluation results_

<div data-search-exclude markdown="1">

URI: [nexus:hasEvaluationResults](https://w3id.org/ai-atlas-nexus/hasEvaluationResults)

<!-- no inheritance hierarchy -->

## Applicable Classes

| Name                                      | Description                                                                      | Modifies Slot |
| ----------------------------------------- | -------------------------------------------------------------------------------- | ------------- |
| [EveryEvalAIResult](EveryEvalAIResult.md) | An evaluation result from the Every Eval Ever dataset, capturing evaluation m... | no            |

## Properties

### Type and Range

| Property  | Value                                               |
| --------- | --------------------------------------------------- |
| Range     | [EvaluationResultRecord](EvaluationResultRecord.md) |
| Domain    | [EveryEvalAIResult](EveryEvalAIResult.md)           |
| Domain Of | [EveryEvalAIResult](EveryEvalAIResult.md)           |

### Cardinality and Requirements

| Property    | Value |
| ----------- | ----- |
| Multivalued | Yes   |

## Identifier and Mapping Information

### Schema Source

- from schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology

## Mappings

| Mapping Type | Mapped Value               |
| ------------ | -------------------------- |
| self         | nexus:hasEvaluationResults |
| native       | nexus:hasEvaluationResults |

## LinkML Source

<details>
```yaml
name: hasEvaluationResults
description: Array of evaluation results
from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
rank: 1000
domain: EveryEvalAIResult
domain_of:
- EveryEvalAIResult
range: EvaluationResultRecord
multivalued: true
inlined: true

```
</details></div>
```
