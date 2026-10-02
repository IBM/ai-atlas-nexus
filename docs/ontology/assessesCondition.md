---
search:
  boost: 5.0
---

# Slot: assessesCondition

_The condition of the evaluation standard that is assessed._

<div data-search-exclude markdown="1">

URI: [earl:test](http://www.w3.org/ns/earl#test)

<!-- no inheritance hierarchy -->

## Applicable Classes

| Name                                          | Description                                                                      | Modifies Slot |
| --------------------------------------------- | -------------------------------------------------------------------------------- | ------------- |
| [ConditionAssessment](ConditionAssessment.md) | One answer of a completed checklist, for one condition of the evaluation stan... | yes           |

## Properties

### Type and Range

| Property  | Value                                         |
| --------- | --------------------------------------------- |
| Range     | [ControlActivity](ControlActivity.md)         |
| Domain Of | [ConditionAssessment](ConditionAssessment.md) |
| Slot URI  | [earl:test](http://www.w3.org/ns/earl#test)   |

### Cardinality and Requirements

| Property | Value |
| -------- | ----- |

## Identifier and Mapping Information

### Schema Source

- from schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology

## Mappings

| Mapping Type | Mapped Value            |
| ------------ | ----------------------- |
| self         | earl:test               |
| native       | nexus:assessesCondition |

## LinkML Source

<details>
```yaml
name: assessesCondition
description: The condition of the evaluation standard that is assessed.
from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
rank: 1000
slot_uri: earl:test
domain_of:
- ConditionAssessment
range: ControlActivity
inlined: false

```
</details></div>
```
