---
search:
  boost: 5.0
---

# Slot: justification

_Why a condition was not fulfilled, or how the same principle was achieved via alternative means._

<div data-search-exclude markdown="1">

URI: [nexus:justification](https://w3id.org/ai-atlas-nexus/justification)

<!-- no inheritance hierarchy -->

## Applicable Classes

| Name                                          | Description                                                                      | Modifies Slot |
| --------------------------------------------- | -------------------------------------------------------------------------------- | ------------- |
| [ConditionAssessment](ConditionAssessment.md) | One answer of a completed checklist, for one condition of the evaluation stan... | no            |

## Properties

### Type and Range

| Property  | Value                                                                |
| --------- | -------------------------------------------------------------------- |
| Range     | [String](String.md)                                                  |
| Domain Of | [ConditionAssessment](ConditionAssessment.md)                        |
| Slot URI  | [nexus:justification](https://w3id.org/ai-atlas-nexus/justification) |

### Cardinality and Requirements

| Property | Value |
| -------- | ----- |

## Identifier and Mapping Information

### Schema Source

- from schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology

## Mappings

| Mapping Type | Mapped Value        |
| ------------ | ------------------- |
| self         | nexus:justification |
| native       | nexus:justification |
| related      | earl:info           |

## LinkML Source

<details>
```yaml
name: justification
description: Why a condition was not fulfilled, or how the same principle was achieved
  via alternative means.
from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
related_mappings:
- earl:info
rank: 1000
slot_uri: nexus:justification
domain_of:
- ConditionAssessment
range: string

```
</details></div>
```
