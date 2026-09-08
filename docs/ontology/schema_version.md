---
search:
  boost: 5.0
---

# Slot: schema_version

_Version of the evaluation schema_

<div data-search-exclude markdown="1">

URI: [nexus:schema_version](https://w3id.org/ai-atlas-nexus/schema_version)

<!-- no inheritance hierarchy -->

## Applicable Classes

| Name                                      | Description                                                                      | Modifies Slot |
| ----------------------------------------- | -------------------------------------------------------------------------------- | ------------- |
| [EveryEvalAIResult](EveryEvalAIResult.md) | An evaluation result from the Every Eval Ever dataset, capturing evaluation m... | no            |

## Properties

### Type and Range

| Property  | Value                                     |
| --------- | ----------------------------------------- |
| Range     | [String](String.md)                       |
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

| Mapping Type | Mapped Value         |
| ------------ | -------------------- |
| self         | nexus:schema_version |
| native       | nexus:schema_version |

## LinkML Source

<details>
```yaml
name: schema_version
description: Version of the evaluation schema
from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
rank: 1000
owner: EveryEvalAIResult
domain_of:
- EveryEvalAIResult
range: string

```
</details></div>
```
