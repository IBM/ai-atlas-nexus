---
search:
  boost: 5.0
---

# Slot: usesEvaluation

_The benchmarks, metrics, or other AI evaluations run as part of the engagement._

<div data-search-exclude markdown="1">

URI: [nexus:usesEvaluation](https://w3id.org/ai-atlas-nexus/usesEvaluation)

<!-- no inheritance hierarchy -->

## Applicable Classes

| Name                                                                | Description                                                                      | Modifies Slot |
| ------------------------------------------------------------------- | -------------------------------------------------------------------------------- | ------------- |
| [ThirdPartyEvaluationEngagement](ThirdPartyEvaluationEngagement.md) | A single engagement in which an independent third-party evaluator evaluates o... | no            |

## Properties

### Type and Range

| Property  | Value                                                                  |
| --------- | ---------------------------------------------------------------------- |
| Range     | [AiEval](AiEval.md)                                                    |
| Domain Of | [ThirdPartyEvaluationEngagement](ThirdPartyEvaluationEngagement.md)    |
| Slot URI  | [nexus:usesEvaluation](https://w3id.org/ai-atlas-nexus/usesEvaluation) |

### Cardinality and Requirements

| Property    | Value |
| ----------- | ----- |
| Multivalued | Yes   |

## Identifier and Mapping Information

### Schema Source

- from schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology

## Mappings

| Mapping Type | Mapped Value         |
| ------------ | -------------------- |
| self         | nexus:usesEvaluation |
| native       | nexus:usesEvaluation |
| close        | prov:used            |

## LinkML Source

<details>
```yaml
name: usesEvaluation
description: The benchmarks, metrics, or other AI evaluations run as part of the engagement.
from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
close_mappings:
- prov:used
rank: 1000
slot_uri: nexus:usesEvaluation
domain_of:
- ThirdPartyEvaluationEngagement
range: AiEval
multivalued: true
inlined: false

```
</details></div>
```
