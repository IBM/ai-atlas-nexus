---
search:
  boost: 5.0
---

# Slot: hasParentDefinition

_Indicates parent terms associated with a term_

<div data-search-exclude markdown="1">

URI: [nexus:hasParentDefinition](https://w3id.org/ai-atlas-nexus/hasParentDefinition)

<!-- no inheritance hierarchy -->

## Applicable Classes

| Name            | Description                | Modifies Slot |
| --------------- | -------------------------- | ------------- |
| [Term](Term.md) | A term and its definitions | no            |

## Properties

### Type and Range

| Property  | Value                                                                            |
| --------- | -------------------------------------------------------------------------------- |
| Range     | [Term](Term.md)                                                                  |
| Domain Of | [Term](Term.md)                                                                  |
| Slot URI  | [nexus:hasParentDefinition](https://w3id.org/ai-atlas-nexus/hasParentDefinition) |

### Cardinality and Requirements

| Property    | Value |
| ----------- | ----- |
| Multivalued | Yes   |

## Identifier and Mapping Information

### Schema Source

- from schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology

## Mappings

| Mapping Type | Mapped Value              |
| ------------ | ------------------------- |
| self         | nexus:hasParentDefinition |
| native       | nexus:hasParentDefinition |

## LinkML Source

<details>
```yaml
name: hasParentDefinition
description: Indicates parent terms associated with a term
from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
rank: 1000
slot_uri: nexus:hasParentDefinition
domain_of:
- Term
range: Term
multivalued: true
inlined: false

```
</details></div>
```
