---
search:
  boost: 5.0
---

# Slot: hasSourceMetadata

_Source metadata for the evaluation_

<div data-search-exclude markdown="1">

URI: [nexus:hasSourceMetadata](https://w3id.org/ai-atlas-nexus/hasSourceMetadata)

<!-- no inheritance hierarchy -->

## Applicable Classes

| Name                                      | Description                                                                      | Modifies Slot |
| ----------------------------------------- | -------------------------------------------------------------------------------- | ------------- |
| [EveryEvalAIResult](EveryEvalAIResult.md) | An evaluation result from the Every Eval Ever dataset, capturing evaluation m... | no            |

## Properties

### Type and Range

| Property  | Value                                     |
| --------- | ----------------------------------------- |
| Range     | [SourceMetadata](SourceMetadata.md)       |
| Domain    | [EveryEvalAIResult](EveryEvalAIResult.md) |
| Domain Of | [EveryEvalAIResult](EveryEvalAIResult.md) |

### Cardinality and Requirements

| Property | Value |
| -------- | ----- |

## Identifier and Mapping Information

### Schema Source

- from schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology

## Mappings

| Mapping Type | Mapped Value            |
| ------------ | ----------------------- |
| self         | nexus:hasSourceMetadata |
| native       | nexus:hasSourceMetadata |

## LinkML Source

<details>
```yaml
name: hasSourceMetadata
description: Source metadata for the evaluation
from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
rank: 1000
domain: EveryEvalAIResult
domain_of:
- EveryEvalAIResult
range: SourceMetadata
inlined: true

```
</details></div>
```
