---
search:
  boost: 5.0
---

# Slot: evidence

_Evidence provides a source (typical a chunk, paragraph or link) describing where some value was found or how it was generated._

<div data-search-exclude markdown="1">

URI: [nexus:evidence](https://w3id.org/ai-atlas-nexus/evidence)
Alias: evidence

<!-- no inheritance hierarchy -->

## Applicable Classes

| Name                                      | Description                                                                      | Modifies Slot |
| ----------------------------------------- | -------------------------------------------------------------------------------- | ------------- |
| [EveryEvalAIResult](EveryEvalAIResult.md) | An evaluation result from the Every Eval Ever dataset, capturing evaluation m... | no            |
| [AiEvalResult](AiEvalResult.md)           | The result of an evaluation for a specific AI model                              | no            |
| [Fact](Fact.md)                           | A fact about something, for example the result of a measurement                  | no            |

## Properties

### Type and Range

| Property  | Value               |
| --------- | ------------------- |
| Range     | [String](String.md) |
| Domain Of | [Fact](Fact.md)     |

### Cardinality and Requirements

| Property | Value |
| -------- | ----- |

## Identifier and Mapping Information

### Schema Source

- from schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology

## Mappings

| Mapping Type | Mapped Value   |
| ------------ | -------------- |
| self         | nexus:evidence |
| native       | nexus:evidence |

## LinkML Source

<details>
```yaml
name: evidence
description: Evidence provides a source (typical a chunk, paragraph or link) describing
  where some value was found or how it was generated.
from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
rank: 1000
alias: evidence
domain_of:
- Fact
range: string

```
</details></div>
```
