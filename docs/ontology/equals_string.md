---
search:
  boost: 5.0
---

# Slot: equals_string

_The string value that the slot must equal to satisfy this condition._

<div data-search-exclude markdown="1">

URI: [nexus:equals_string](https://w3id.org/ai-atlas-nexus/equals_string)

<!-- no inheritance hierarchy -->

## Applicable Classes

| Name                              | Description | Modifies Slot |
| --------------------------------- | ----------- | ------------- |
| [SlotCondition](SlotCondition.md) |             | no            |

## Properties

### Type and Range

| Property  | Value                             |
| --------- | --------------------------------- |
| Range     | [String](String.md)               |
| Domain Of | [SlotCondition](SlotCondition.md) |

### Cardinality and Requirements

| Property | Value |
| -------- | ----- |

### Slot Characteristics

| Property | Value                             |
| -------- | --------------------------------- |
| Owner    | [SlotCondition](SlotCondition.md) |

## Identifier and Mapping Information

### Schema Source

- from schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology

## Mappings

| Mapping Type | Mapped Value        |
| ------------ | ------------------- |
| self         | nexus:equals_string |
| native       | nexus:equals_string |

## LinkML Source

<details>
```yaml
name: equals_string
description: The string value that the slot must equal to satisfy this condition.
from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
rank: 1000
owner: SlotCondition
domain_of:
- SlotCondition
range: string

```
</details></div>
```
