---
search:
  boost: 5.0
---

# Slot: hasKeywords

_A collection of keywords_

<div data-search-exclude markdown="1">

URI: [nexus:hasKeywords](https://w3id.org/ai-atlas-nexus/hasKeywords)

<!-- no inheritance hierarchy -->

## Applicable Classes

| Name                          | Description                                                                      | Modifies Slot |
| ----------------------------- | -------------------------------------------------------------------------------- | ------------- |
| [Requirement](Requirement.md) | A requirement representing a combination of obligation, permission, or prohib... | no            |

## Properties

### Type and Range

| Property  | Value                                                            |
| --------- | ---------------------------------------------------------------- |
| Range     | [String](String.md)                                              |
| Domain    | [Requirement](Requirement.md)                                    |
| Domain Of | [Requirement](Requirement.md)                                    |
| Slot URI  | [nexus:hasKeywords](https://w3id.org/ai-atlas-nexus/hasKeywords) |

### Cardinality and Requirements

| Property    | Value |
| ----------- | ----- |
| Multivalued | Yes   |

## Identifier and Mapping Information

### Schema Source

- from schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology

## Mappings

| Mapping Type | Mapped Value      |
| ------------ | ----------------- |
| self         | nexus:hasKeywords |
| native       | nexus:hasKeywords |

## LinkML Source

<details>
```yaml
name: hasKeywords
description: A collection of keywords
from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
rank: 1000
domain: Requirement
slot_uri: nexus:hasKeywords
domain_of:
- Requirement
range: string
multivalued: true
inlined: false

```
</details></div>
```
