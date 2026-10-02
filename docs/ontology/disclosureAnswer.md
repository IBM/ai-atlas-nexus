---
search:
  boost: 5.0
---

# Slot: disclosureAnswer

_For disclosure conditions (e.g. AEF-1 2.4.x), whether the disclosed circumstance applies, e.g. true if the evaluator was paid by the system provider. Independent of whether the condition was fulfilled._

<div data-search-exclude markdown="1">

URI: [nexus:disclosureAnswer](https://w3id.org/ai-atlas-nexus/disclosureAnswer)

<!-- no inheritance hierarchy -->

## Applicable Classes

| Name                                          | Description                                                                      | Modifies Slot |
| --------------------------------------------- | -------------------------------------------------------------------------------- | ------------- |
| [ConditionAssessment](ConditionAssessment.md) | One answer of a completed checklist, for one condition of the evaluation stan... | no            |

## Properties

### Type and Range

| Property  | Value                                                                      |
| --------- | -------------------------------------------------------------------------- |
| Range     | [Boolean](Boolean.md)                                                      |
| Domain Of | [ConditionAssessment](ConditionAssessment.md)                              |
| Slot URI  | [nexus:disclosureAnswer](https://w3id.org/ai-atlas-nexus/disclosureAnswer) |

### Cardinality and Requirements

| Property | Value |
| -------- | ----- |

## Identifier and Mapping Information

### Schema Source

- from schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology

## Mappings

| Mapping Type | Mapped Value           |
| ------------ | ---------------------- |
| self         | nexus:disclosureAnswer |
| native       | nexus:disclosureAnswer |

## LinkML Source

<details>
```yaml
name: disclosureAnswer
description: For disclosure conditions (e.g. AEF-1 2.4.x), whether the disclosed circumstance
  applies, e.g. true if the evaluator was paid by the system provider. Independent
  of whether the condition was fulfilled.
from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
rank: 1000
slot_uri: nexus:disclosureAnswer
domain_of:
- ConditionAssessment
range: boolean

```
</details></div>
```
