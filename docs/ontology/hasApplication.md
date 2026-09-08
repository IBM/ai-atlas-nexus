---
search:
  boost: 5.0
---

# Slot: hasApplication

_The application category, Optional or Mandatory._

<div data-search-exclude markdown="1">

URI: [nexus:hasApplication](https://w3id.org/ai-atlas-nexus/hasApplication)

<!-- no inheritance hierarchy -->

## Applicable Classes

| Name                          | Description                                                                      | Modifies Slot |
| ----------------------------- | -------------------------------------------------------------------------------- | ------------- |
| [Requirement](Requirement.md) | A requirement representing a combination of obligation, permission, or prohib... | no            |

## Properties

### Type and Range

| Property  | Value                                                                  |
| --------- | ---------------------------------------------------------------------- |
| Range     | [AIUC1ApplicationCategory](AIUC1ApplicationCategory.md)                |
| Domain    | [Requirement](Requirement.md)                                          |
| Domain Of | [Requirement](Requirement.md)                                          |
| Slot URI  | [nexus:hasApplication](https://w3id.org/ai-atlas-nexus/hasApplication) |

### Cardinality and Requirements

| Property    | Value |
| ----------- | ----- |
| Multivalued | Yes   |

## Identifier and Mapping Information

### Schema Source

- from schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology

## Mappings

| Mapping Type | Mapped Value         |
| ------------ | -------------------- |
| self         | nexus:hasApplication |
| native       | nexus:hasApplication |

## LinkML Source

<details>
```yaml
name: hasApplication
description: The application category, Optional or Mandatory.
from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
rank: 1000
domain: Requirement
slot_uri: nexus:hasApplication
domain_of:
- Requirement
range: AIUC1ApplicationCategory
multivalued: true
inlined: false

```
</details></div>
```
