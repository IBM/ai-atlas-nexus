---
search:
  boost: 5.0
---

# Slot: hasSubDefinition

_Indicates child terms associated with a term_

<div data-search-exclude markdown="1">

URI: [nexus:hasSubDefinition](https://w3id.org/ai-atlas-nexus/hasSubDefinition)

<!-- no inheritance hierarchy -->

## Applicable Classes

| Name            | Description                | Modifies Slot |
| --------------- | -------------------------- | ------------- |
| [Term](Term.md) | A term and its definitions | no            |

## Properties

### Type and Range

| Property  | Value                                                                      |
| --------- | -------------------------------------------------------------------------- |
| Range     | [Term](Term.md)                                                            |
| Domain Of | [Term](Term.md)                                                            |
| Slot URI  | [nexus:hasSubDefinition](https://w3id.org/ai-atlas-nexus/hasSubDefinition) |

### Cardinality and Requirements

| Property    | Value |
| ----------- | ----- |
| Multivalued | Yes   |

## Identifier and Mapping Information

### Schema Source

- from schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology

## Mappings

| Mapping Type | Mapped Value           |
| ------------ | ---------------------- |
| self         | nexus:hasSubDefinition |
| native       | nexus:hasSubDefinition |

## LinkML Source

<details>
```yaml
name: hasSubDefinition
description: Indicates child terms associated with a term
from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
rank: 1000
slot_uri: nexus:hasSubDefinition
domain_of:
- Term
range: Term
multivalued: true
inlined: false

```
</details></div>
```
