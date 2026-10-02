---
search:
  boost: 5.0
---

# Slot: endDate

_The date on which the entity ended._

<div data-search-exclude markdown="1">

URI: [schema:endDate](http://schema.org/endDate)

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
| Slot URI  | [schema:endDate](http://schema.org/endDate)                         |

### Cardinality and Requirements

| Property | Value |
| -------- | ----- |

## Identifier and Mapping Information

### Schema Source

- from schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology

## Mappings

| Mapping Type | Mapped Value     |
| ------------ | ---------------- |
| self         | schema:endDate   |
| native       | nexus:endDate    |
| close        | prov:endedAtTime |

## LinkML Source

<details>
```yaml
name: endDate
description: The date on which the entity ended.
from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
close_mappings:
- prov:endedAtTime
rank: 1000
slot_uri: schema:endDate
domain_of:
- ThirdPartyEvaluationEngagement
range: date

```
</details></div>
```
