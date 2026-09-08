---
search:
  boost: 5.0
---

# Slot: score

_The evaluation score_

<div data-search-exclude markdown="1">

URI: [nexus:score](https://w3id.org/ai-atlas-nexus/score)

<!-- no inheritance hierarchy -->

## Applicable Classes

| Name                            | Description                     | Modifies Slot |
| ------------------------------- | ------------------------------- | ------------- |
| [ScoreDetails](ScoreDetails.md) | Details about evaluation scores | no            |

## Properties

### Type and Range

| Property  | Value                           |
| --------- | ------------------------------- |
| Range     | [Float](Float.md)               |
| Domain Of | [ScoreDetails](ScoreDetails.md) |

### Cardinality and Requirements

| Property | Value |
| -------- | ----- |

### Slot Characteristics

| Property | Value                           |
| -------- | ------------------------------- |
| Owner    | [ScoreDetails](ScoreDetails.md) |

## Identifier and Mapping Information

### Schema Source

- from schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology

## Mappings

| Mapping Type | Mapped Value |
| ------------ | ------------ |
| self         | nexus:score  |
| native       | nexus:score  |

## LinkML Source

<details>
```yaml
name: score
description: The evaluation score
from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
rank: 1000
owner: ScoreDetails
domain_of:
- ScoreDetails
range: float

```
</details></div>
```
