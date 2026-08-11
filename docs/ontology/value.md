---
search:
  boost: 5.0
---

# Slot: value

_Some numeric or string value_

<div data-search-exclude markdown="1">

URI: [nexus:value](https://w3id.org/ai-atlas-nexus/value)
Alias: value

<!-- no inheritance hierarchy -->

## Applicable Classes

| Name                                      | Description                                                                      | Modifies Slot |
| ----------------------------------------- | -------------------------------------------------------------------------------- | ------------- |
| [AiEvalResult](AiEvalResult.md)           | The result of an evaluation for a specific AI model                              | no            |
| [Fact](Fact.md)                           | A fact about something, for example the result of a measurement                  | no            |
| [EveryEvalAIResult](EveryEvalAIResult.md) | An evaluation result from the Every Eval Ever dataset, capturing evaluation m... | no            |

## Properties

### Type and Range

| Property  | Value               |
| --------- | ------------------- |
| Range     | [String](String.md) |
| Domain Of | [Fact](Fact.md)     |

### Cardinality and Requirements

| Property | Value |
| -------- | ----- |
| Required | Yes   |

## Identifier and Mapping Information

### Schema Source

- from schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology

## Mappings

| Mapping Type | Mapped Value |
| ------------ | ------------ |
| self         | nexus:value  |
| native       | nexus:value  |

## LinkML Source

<details>
```yaml
name: value
description: Some numeric or string value
from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
rank: 1000
alias: value
domain_of:
- Fact
range: string
required: true

```
</details></div>
```
