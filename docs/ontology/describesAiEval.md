# Slot: describesAiEval

_A relationship where a BenchmarkMetadataCard describes and AI evaluation (benchmark)._

URI: [nexus:describesAiEval](https://ibm.github.io/ai-atlas-nexus/ontology/describesAiEval)
Alias: describesAiEval

<!-- no inheritance hierarchy -->

## Applicable Classes

| Name                                              | Description                                                                      | Modifies Slot |
| ------------------------------------------------- | -------------------------------------------------------------------------------- | ------------- |
| [BenchmarkMetadataCard](BenchmarkMetadataCard.md) | Benchmark metadata cards offer a standardized way to document LLM benchmarks ... | no            |

## Properties

### Type and Range

| Property  | Value                                             |
| --------- | ------------------------------------------------- |
| Range     | [AiEval](AiEval.md)                               |
| Domain    | [BenchmarkMetadataCard](BenchmarkMetadataCard.md) |
| Domain Of | [BenchmarkMetadataCard](BenchmarkMetadataCard.md) |

### Cardinality and Requirements

| Property    | Value |
| ----------- | ----- |
| Multivalued | Yes   |

<details>
<summary>Relationship Properties</summary>

| Property | Value                                           |
| -------- | ----------------------------------------------- |
| Inverse  | [hasBenchmarkMetadata](hasBenchmarkMetadata.md) |

</details>

## Identifier and Mapping Information

### Schema Source

- from schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology

## Mappings

| Mapping Type | Mapped Value          |
| ------------ | --------------------- |
| self         | nexus:describesAiEval |
| native       | nexus:describesAiEval |

## LinkML Source

<details>
```yaml
name: describesAiEval
description: A relationship where a BenchmarkMetadataCard describes and AI evaluation
  (benchmark).
from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
rank: 1000
domain: BenchmarkMetadataCard
alias: describesAiEval
domain_of:
- BenchmarkMetadataCard
inverse: hasBenchmarkMetadata
range: AiEval
multivalued: true
inlined: false

```
</details>
```
