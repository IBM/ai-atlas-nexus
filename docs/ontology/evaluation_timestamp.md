---
search:
  boost: 5.0
---

# Slot: evaluation_timestamp

_ISO 8601 timestamp when evaluation was performed_

<div data-search-exclude markdown="1">

URI: [nexus:evaluation_timestamp](https://w3id.org/ai-atlas-nexus/evaluation_timestamp)

<!-- no inheritance hierarchy -->

## Applicable Classes

| Name                                      | Description                                                                      | Modifies Slot |
| ----------------------------------------- | -------------------------------------------------------------------------------- | ------------- |
| [EveryEvalAIResult](EveryEvalAIResult.md) | An evaluation result from the Every Eval Ever dataset, capturing evaluation m... | no            |

## Properties

### Type and Range

| Property  | Value                                     |
| --------- | ----------------------------------------- |
| Range     | [Datetime](Datetime.md)                   |
| Domain Of | [EveryEvalAIResult](EveryEvalAIResult.md) |

### Cardinality and Requirements

| Property | Value |
| -------- | ----- |

### Slot Characteristics

| Property | Value                                     |
| -------- | ----------------------------------------- |
| Owner    | [EveryEvalAIResult](EveryEvalAIResult.md) |

## Identifier and Mapping Information

### Schema Source

- from schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology

## Mappings

| Mapping Type | Mapped Value               |
| ------------ | -------------------------- |
| self         | nexus:evaluation_timestamp |
| native       | nexus:evaluation_timestamp |

## LinkML Source

<details>
```yaml
name: evaluation_timestamp
description: ISO 8601 timestamp when evaluation was performed
from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
rank: 1000
owner: EveryEvalAIResult
domain_of:
- EveryEvalAIResult
range: datetime

```
</details></div>
```
