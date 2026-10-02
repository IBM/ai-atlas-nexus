---
search:
  boost: 5.0
---

# Slot: hasConformanceOutcome

_Whether the condition was fulfilled._

<div data-search-exclude markdown="1">

URI: [earl:outcome](http://www.w3.org/ns/earl#outcome)

<!-- no inheritance hierarchy -->

## Applicable Classes

| Name                                          | Description                                                                      | Modifies Slot |
| --------------------------------------------- | -------------------------------------------------------------------------------- | ------------- |
| [ConditionAssessment](ConditionAssessment.md) | One answer of a completed checklist, for one condition of the evaluation stan... | yes           |

## Properties

### Type and Range

| Property  | Value                                             |
| --------- | ------------------------------------------------- |
| Range     | [ConformanceOutcome](ConformanceOutcome.md)       |
| Domain Of | [ConditionAssessment](ConditionAssessment.md)     |
| Slot URI  | [earl:outcome](http://www.w3.org/ns/earl#outcome) |

### Cardinality and Requirements

| Property | Value |
| -------- | ----- |

## Identifier and Mapping Information

### Schema Source

- from schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology

## Mappings

| Mapping Type | Mapped Value                |
| ------------ | --------------------------- |
| self         | earl:outcome                |
| native       | nexus:hasConformanceOutcome |
| close        | dpv:hasComplianceStatus     |

## LinkML Source

<details>
```yaml
name: hasConformanceOutcome
description: Whether the condition was fulfilled.
from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
close_mappings:
- dpv:hasComplianceStatus
rank: 1000
slot_uri: earl:outcome
domain_of:
- ConditionAssessment
range: ConformanceOutcome

```
</details></div>
```
