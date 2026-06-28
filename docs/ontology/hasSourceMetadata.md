# Slot: hasSourceMetadata

_Source metadata for the evaluation_

URI: [nexus:hasSourceMetadata](https://ibm.github.io/ai-atlas-nexus/ontology/hasSourceMetadata)
Alias: hasSourceMetadata

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

- from schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology

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
from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
rank: 1000
domain: EveryEvalAIResult
alias: hasSourceMetadata
domain_of:
- EveryEvalAIResult
range: SourceMetadata
inlined: true

```
</details>
```
