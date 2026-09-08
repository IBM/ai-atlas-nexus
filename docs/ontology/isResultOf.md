---
search:
  boost: 5.0
---

# Slot: isResultOf

_A relationship indicating that an entity is the result of an AI evaluation._

<div data-search-exclude markdown="1">

URI: [dqv:isMeasurementOf](https://www.w3.org/TR/vocab-dqv/isMeasurementOf)

<!-- no inheritance hierarchy -->

## Applicable Classes

| Name                                      | Description                                                                      | Modifies Slot |
| ----------------------------------------- | -------------------------------------------------------------------------------- | ------------- |
| [AiEvalResult](AiEvalResult.md)           | The result of an evaluation for a specific AI model                              | no            |
| [EveryEvalAIResult](EveryEvalAIResult.md) | An evaluation result from the Every Eval Ever dataset, capturing evaluation m... | no            |

## Properties

### Type and Range

| Property  | Value                                                                  |
| --------- | ---------------------------------------------------------------------- |
| Range     | [AiEval](AiEval.md)                                                    |
| Domain Of | [AiEvalResult](AiEvalResult.md)                                        |
| Slot URI  | [dqv:isMeasurementOf](https://www.w3.org/TR/vocab-dqv/isMeasurementOf) |

### Cardinality and Requirements

| Property | Value |
| -------- | ----- |

## Identifier and Mapping Information

### Schema Source

- from schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology

## Mappings

| Mapping Type | Mapped Value        |
| ------------ | ------------------- |
| self         | dqv:isMeasurementOf |
| native       | nexus:isResultOf    |

## LinkML Source

<details>
```yaml
name: isResultOf
description: A relationship indicating that an entity is the result of an AI evaluation.
from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
rank: 1000
slot_uri: dqv:isMeasurementOf
domain_of:
- AiEvalResult
range: AiEval
multivalued: false
inlined: false

```
</details></div>
```
