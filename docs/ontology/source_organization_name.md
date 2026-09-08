---
search:
  boost: 5.0
---

# Slot: source_organization_name

_Organization that provided the evaluation_

<div data-search-exclude markdown="1">

URI: [nexus:source_organization_name](https://w3id.org/ai-atlas-nexus/source_organization_name)

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

| Mapping Type | Mapped Value                   |
| ------------ | ------------------------------ |
| self         | nexus:source_organization_name |
| native       | nexus:source_organization_name |

## LinkML Source

<details>
```yaml
name: source_organization_name
description: Organization that provided the evaluation
from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
rank: 1000
owner: SourceMetadata
domain_of:
- SourceMetadata
range: string

```
</details></div>
```
