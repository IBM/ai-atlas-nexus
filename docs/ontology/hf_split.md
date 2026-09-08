---
search:
  boost: 5.0
---

# Slot: hf_split

_HuggingFace dataset split_

<div data-search-exclude markdown="1">

URI: [nexus:hf_split](https://w3id.org/ai-atlas-nexus/hf_split)

<!-- no inheritance hierarchy -->

## Applicable Classes

| Name                        | Description                                          | Modifies Slot |
| --------------------------- | ---------------------------------------------------- | ------------- |
| [SourceData](SourceData.md) | Information about the data source used in evaluation | no            |

## Properties

### Type and Range

| Property  | Value                       |
| --------- | --------------------------- |
| Range     | [String](String.md)         |
| Domain Of | [SourceData](SourceData.md) |

### Cardinality and Requirements

| Property | Value |
| -------- | ----- |

### Slot Characteristics

| Property | Value                       |
| -------- | --------------------------- |
| Owner    | [SourceData](SourceData.md) |

## Identifier and Mapping Information

### Schema Source

- from schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology

## Mappings

| Mapping Type | Mapped Value   |
| ------------ | -------------- |
| self         | nexus:hf_split |
| native       | nexus:hf_split |

## LinkML Source

<details>
```yaml
name: hf_split
description: HuggingFace dataset split
from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
rank: 1000
owner: SourceData
domain_of:
- SourceData
range: string

```
</details></div>
```
