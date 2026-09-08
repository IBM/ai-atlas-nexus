---
search:
  boost: 5.0
---

# Slot: model_name

_Name of the AI model_

<div data-search-exclude markdown="1">

URI: [nexus:model_name](https://w3id.org/ai-atlas-nexus/model_name)

<!-- no inheritance hierarchy -->

## Applicable Classes

| Name                      | Description                                    | Modifies Slot |
| ------------------------- | ---------------------------------------------- | ------------- |
| [ModelInfo](ModelInfo.md) | Information about the AI model being evaluated | no            |

## Properties

### Type and Range

| Property  | Value                     |
| --------- | ------------------------- |
| Range     | [String](String.md)       |
| Domain Of | [ModelInfo](ModelInfo.md) |

### Cardinality and Requirements

| Property | Value |
| -------- | ----- |

### Slot Characteristics

| Property | Value                     |
| -------- | ------------------------- |
| Owner    | [ModelInfo](ModelInfo.md) |

## Identifier and Mapping Information

### Schema Source

- from schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology

## Mappings

| Mapping Type | Mapped Value     |
| ------------ | ---------------- |
| self         | nexus:model_name |
| native       | nexus:model_name |

## LinkML Source

<details>
```yaml
name: model_name
description: Name of the AI model
from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
rank: 1000
owner: ModelInfo
domain_of:
- ModelInfo
range: string

```
</details></div>
```
