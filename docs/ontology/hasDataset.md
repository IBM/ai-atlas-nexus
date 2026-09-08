---
search:
  boost: 5.0
---

# Slot: hasDataset

_A relationship to datasets that are used._

<div data-search-exclude markdown="1">

URI: [nexus:hasDataset](https://w3id.org/ai-atlas-nexus/hasDataset)

<!-- no inheritance hierarchy -->

## Applicable Classes

| Name                              | Description                                       | Modifies Slot |
| --------------------------------- | ------------------------------------------------- | ------------- |
| [AiEval](AiEval.md)               | An AI Evaluation, e                               | no            |
| [Question](Question.md)           | An evaluation where a question has to be answered | no            |
| [Questionnaire](Questionnaire.md) | A questionnaire groups questions                  | no            |

## Properties

### Type and Range

| Property  | Value                 |
| --------- | --------------------- |
| Range     | [Dataset](Dataset.md) |
| Domain Of | [AiEval](AiEval.md)   |

### Cardinality and Requirements

| Property    | Value |
| ----------- | ----- |
| Multivalued | Yes   |

## Identifier and Mapping Information

### Schema Source

- from schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology

## Mappings

| Mapping Type | Mapped Value     |
| ------------ | ---------------- |
| self         | nexus:hasDataset |
| native       | nexus:hasDataset |

## LinkML Source

<details>
```yaml
name: hasDataset
description: A relationship to datasets that are used.
from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
rank: 1000
domain_of:
- AiEval
range: Dataset
multivalued: true
inlined: false

```
</details></div>
```
