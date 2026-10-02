---
search:
  boost: 5.0
---

# Slot: hasPrinciple

_The principle(s) this entry is composed of or belongs to_

<div data-search-exclude markdown="1">

URI: [dpv:isPartOf](https://w3id.org/dpv#isPartOf)

<!-- no inheritance hierarchy -->

## Applicable Classes

| Name                                        | Description                                                                      | Modifies Slot |
| ------------------------------------------- | -------------------------------------------------------------------------------- | ------------- |
| [EvaluationStandard](EvaluationStandard.md) | A standard defining minimum conditions, processes, or independence criteria r... | no            |
| [Requirement](Requirement.md)               | A requirement representing a combination of obligation, permission, or prohib... | no            |

## Properties

### Type and Range

| Property  | Value                                                                      |
| --------- | -------------------------------------------------------------------------- |
| Range     | [Principle](Principle.md)                                                  |
| Domain    | [Entry](Entry.md)                                                          |
| Domain Of | [EvaluationStandard](EvaluationStandard.md), [Requirement](Requirement.md) |
| Slot URI  | [dpv:isPartOf](https://w3id.org/dpv#isPartOf)                              |

### Cardinality and Requirements

| Property    | Value |
| ----------- | ----- |
| Multivalued | Yes   |

## Identifier and Mapping Information

### Schema Source

- from schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology

## Mappings

| Mapping Type | Mapped Value       |
| ------------ | ------------------ |
| self         | dpv:isPartOf       |
| native       | nexus:hasPrinciple |

## LinkML Source

<details>
```yaml
name: hasPrinciple
description: The principle(s) this entry is composed of or belongs to
from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
rank: 1000
domain: Entry
slot_uri: dpv:isPartOf
domain_of:
- EvaluationStandard
- Requirement
range: Principle
multivalued: true
inlined: false

```
</details></div>
```
