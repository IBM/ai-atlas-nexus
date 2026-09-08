---
search:
  boost: 5.0
---

# Slot: hasModelInfo

_Model information for the evaluation_

<div data-search-exclude markdown="1">

URI: [nexus:hasModelInfo](https://w3id.org/ai-atlas-nexus/hasModelInfo)

<!-- no inheritance hierarchy -->

## Applicable Classes

| Name                                      | Description                                                                      | Modifies Slot |
| ----------------------------------------- | -------------------------------------------------------------------------------- | ------------- |
| [EveryEvalAIResult](EveryEvalAIResult.md) | An evaluation result from the Every Eval Ever dataset, capturing evaluation m... | no            |

## Properties

### Type and Range

| Property  | Value                                     |
| --------- | ----------------------------------------- |
| Range     | [ModelInfo](ModelInfo.md)                 |
| Domain    | [EveryEvalAIResult](EveryEvalAIResult.md) |
| Domain Of | [EveryEvalAIResult](EveryEvalAIResult.md) |

### Cardinality and Requirements

| Property | Value |
| -------- | ----- |

## Identifier and Mapping Information

### Schema Source

- from schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology

## Mappings

| Mapping Type | Mapped Value       |
| ------------ | ------------------ |
| self         | nexus:hasModelInfo |
| native       | nexus:hasModelInfo |

## LinkML Source

<details>
```yaml
name: hasModelInfo
description: Model information for the evaluation
from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
rank: 1000
domain: EveryEvalAIResult
domain_of:
- EveryEvalAIResult
range: ModelInfo
inlined: true

```
</details></div>
```
