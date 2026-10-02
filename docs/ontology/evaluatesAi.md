---
search:
  boost: 5.0
---

# Slot: evaluatesAi

_The AI systems or models (including specific versions) evaluated in the engagement._

<div data-search-exclude markdown="1">

URI: [nexus:evaluatesAi](https://w3id.org/ai-atlas-nexus/evaluatesAi)

<!-- no inheritance hierarchy -->

## Applicable Classes

| Name                                                                | Description                                                                      | Modifies Slot |
| ------------------------------------------------------------------- | -------------------------------------------------------------------------------- | ------------- |
| [ThirdPartyEvaluationEngagement](ThirdPartyEvaluationEngagement.md) | A single engagement in which an independent third-party evaluator evaluates o... | no            |

## Properties

### Type and Range

| Property  | Value                                                               |
| --------- | ------------------------------------------------------------------- |
| Range     | [BaseAi](BaseAi.md)                                                 |
| Domain Of | [ThirdPartyEvaluationEngagement](ThirdPartyEvaluationEngagement.md) |
| Slot URI  | [nexus:evaluatesAi](https://w3id.org/ai-atlas-nexus/evaluatesAi)    |

### Cardinality and Requirements

| Property    | Value |
| ----------- | ----- |
| Multivalued | Yes   |

## Identifier and Mapping Information

### Schema Source

- from schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology

## Mappings

| Mapping Type | Mapped Value      |
| ------------ | ----------------- |
| self         | nexus:evaluatesAi |
| native       | nexus:evaluatesAi |
| related      | earl:subject      |

## LinkML Source

<details>
```yaml
name: evaluatesAi
description: The AI systems or models (including specific versions) evaluated in the
  engagement.
from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
related_mappings:
- earl:subject
rank: 1000
slot_uri: nexus:evaluatesAi
domain_of:
- ThirdPartyEvaluationEngagement
range: BaseAi
multivalued: true
inlined: false

```
</details></div>
```
