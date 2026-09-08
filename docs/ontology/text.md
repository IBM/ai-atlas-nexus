---
search:
  boost: 5.0
---

# Slot: text

_The question itself_

<div data-search-exclude markdown="1">

URI: [nexus:text](https://w3id.org/ai-atlas-nexus/text)

<!-- no inheritance hierarchy -->

## Applicable Classes

| Name                    | Description                                       | Modifies Slot |
| ----------------------- | ------------------------------------------------- | ------------- |
| [Question](Question.md) | An evaluation where a question has to be answered | no            |

## Properties

### Type and Range

| Property  | Value                   |
| --------- | ----------------------- |
| Range     | [String](String.md)     |
| Domain Of | [Question](Question.md) |

### Cardinality and Requirements

| Property | Value |
| -------- | ----- |
| Required | Yes   |

### Slot Characteristics

| Property | Value                   |
| -------- | ----------------------- |
| Owner    | [Question](Question.md) |

## Identifier and Mapping Information

### Schema Source

- from schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology

## Mappings

| Mapping Type | Mapped Value |
| ------------ | ------------ |
| self         | nexus:text   |
| native       | nexus:text   |

## LinkML Source

<details>
```yaml
name: text
description: The question itself
from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
rank: 1000
owner: Question
domain_of:
- Question
range: string
required: true

```
</details></div>
```
