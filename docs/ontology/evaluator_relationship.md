---
search:
  boost: 5.0
---

# Slot: evaluator_relationship

_Relationship of evaluator (e.g., first_party, third_party)_

<div data-search-exclude markdown="1">

URI: [nexus:evaluator_relationship](https://w3id.org/ai-atlas-nexus/evaluator_relationship)

<!-- no inheritance hierarchy -->

## Applicable Classes

| Name                                | Description                                | Modifies Slot |
| ----------------------------------- | ------------------------------------------ | ------------- |
| [SourceMetadata](SourceMetadata.md) | Metadata about the source of an evaluation | no            |

## Properties

### Type and Range

| Property  | Value                               |
| --------- | ----------------------------------- |
| Range     | [String](String.md)                 |
| Domain Of | [SourceMetadata](SourceMetadata.md) |

### Cardinality and Requirements

| Property | Value |
| -------- | ----- |

### Slot Characteristics

| Property | Value                               |
| -------- | ----------------------------------- |
| Owner    | [SourceMetadata](SourceMetadata.md) |

## Identifier and Mapping Information

### Schema Source

- from schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology

## Mappings

| Mapping Type | Mapped Value                 |
| ------------ | ---------------------------- |
| self         | nexus:evaluator_relationship |
| native       | nexus:evaluator_relationship |

## LinkML Source

<details>
```yaml
name: evaluator_relationship
description: Relationship of evaluator (e.g., first_party, third_party)
from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
rank: 1000
owner: SourceMetadata
domain_of:
- SourceMetadata
range: string

```
</details></div>
```
