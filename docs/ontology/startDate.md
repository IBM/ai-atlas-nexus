---
search:
  boost: 5.0
---

# Slot: startDate

_The date on which the entity started._

<div data-search-exclude markdown="1">

URI: [schema:startDate](http://schema.org/startDate)

<!-- no inheritance hierarchy -->

## Applicable Classes

| Name                                                                | Description                                                                      | Modifies Slot |
| ------------------------------------------------------------------- | -------------------------------------------------------------------------------- | ------------- |
| [ThirdPartyEvaluationEngagement](ThirdPartyEvaluationEngagement.md) | A single engagement in which an independent third-party evaluator evaluates o... | no            |

## Properties

### Type and Range

| Property  | Value                                                               |
| --------- | ------------------------------------------------------------------- |
| Range     | [Date](Date.md)                                                     |
| Domain Of | [ThirdPartyEvaluationEngagement](ThirdPartyEvaluationEngagement.md) |
| Slot URI  | [schema:startDate](http://schema.org/startDate)                     |

### Cardinality and Requirements

| Property | Value |
| -------- | ----- |

## Identifier and Mapping Information

### Schema Source

- from schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology

## Mappings

| Mapping Type | Mapped Value       |
| ------------ | ------------------ |
| self         | schema:startDate   |
| native       | nexus:startDate    |
| close        | prov:startedAtTime |

## LinkML Source

<details>
```yaml
name: startDate
description: The date on which the entity started.
from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
close_mappings:
- prov:startedAtTime
rank: 1000
slot_uri: schema:startDate
domain_of:
- ThirdPartyEvaluationEngagement
range: date

```
</details></div>
```
