---
search:
  boost: 5.0
---

# Slot: hasSystemProvider

_The organization which develops or operates the AI systems being evaluated._

<div data-search-exclude markdown="1">

URI: [nexus:hasSystemProvider](https://w3id.org/ai-atlas-nexus/hasSystemProvider)

<!-- no inheritance hierarchy -->

## Applicable Classes

| Name                                                                | Description                                                                      | Modifies Slot |
| ------------------------------------------------------------------- | -------------------------------------------------------------------------------- | ------------- |
| [ThirdPartyEvaluationEngagement](ThirdPartyEvaluationEngagement.md) | A single engagement in which an independent third-party evaluator evaluates o... | no            |

## Properties

### Type and Range

| Property  | Value                                                                        |
| --------- | ---------------------------------------------------------------------------- |
| Range     | [Organization](Organization.md)                                              |
| Domain Of | [ThirdPartyEvaluationEngagement](ThirdPartyEvaluationEngagement.md)          |
| Slot URI  | [nexus:hasSystemProvider](https://w3id.org/ai-atlas-nexus/hasSystemProvider) |

### Cardinality and Requirements

| Property | Value |
| -------- | ----- |

## Identifier and Mapping Information

### Schema Source

- from schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology

## Mappings

| Mapping Type | Mapped Value            |
| ------------ | ----------------------- |
| self         | nexus:hasSystemProvider |
| native       | nexus:hasSystemProvider |

## LinkML Source

<details>
```yaml
name: hasSystemProvider
description: The organization which develops or operates the AI systems being evaluated.
from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
rank: 1000
slot_uri: nexus:hasSystemProvider
domain_of:
- ThirdPartyEvaluationEngagement
range: Organization
inlined: false

```
</details></div>
```
