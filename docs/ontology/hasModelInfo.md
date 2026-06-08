# Slot: hasModelInfo

_Model information for the evaluation_

URI: [nexus:hasModelInfo](https://ibm.github.io/ai-atlas-nexus/ontology/hasModelInfo)
Alias: hasModelInfo

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

- from schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology

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
from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
rank: 1000
domain: EveryEvalAIResult
alias: hasModelInfo
domain_of:
- EveryEvalAIResult
range: ModelInfo
inlined: true

```
</details>
```
