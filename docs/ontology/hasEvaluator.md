---
search:
  boost: 5.0
---

# Slot: hasEvaluator

_The organization that conducted the evaluation._

<div data-search-exclude markdown="1">

URI: [nexus:hasEvaluator](https://w3id.org/ai-atlas-nexus/hasEvaluator)

<!-- no inheritance hierarchy -->

## Applicable Classes

| Name                                                                | Description                                                                      | Modifies Slot |
| ------------------------------------------------------------------- | -------------------------------------------------------------------------------- | ------------- |
| [ThirdPartyEvaluationEngagement](ThirdPartyEvaluationEngagement.md) | A single engagement in which an independent third-party evaluator evaluates o... | no            |

## Properties

### Type and Range

| Property  | Value                                                               |
| --------- | ------------------------------------------------------------------- |
| Range     | [Organization](Organization.md)                                     |
| Domain Of | [ThirdPartyEvaluationEngagement](ThirdPartyEvaluationEngagement.md) |
| Slot URI  | [nexus:hasEvaluator](https://w3id.org/ai-atlas-nexus/hasEvaluator)  |

### Cardinality and Requirements

| Property | Value |
| -------- | ----- |

## Identifier and Mapping Information

### Schema Source

- from schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology

## Mappings

| Mapping Type | Mapped Value           |
| ------------ | ---------------------- |
| self         | nexus:hasEvaluator     |
| native       | nexus:hasEvaluator     |
| related      | earl:assertedBy        |
| close        | prov:wasAssociatedWith |

## LinkML Source

<details>
```yaml
name: hasEvaluator
description: The organization that conducted the evaluation.
from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
close_mappings:
- prov:wasAssociatedWith
related_mappings:
- earl:assertedBy
rank: 1000
slot_uri: nexus:hasEvaluator
domain_of:
- ThirdPartyEvaluationEngagement
range: Organization
inlined: false

```
</details></div>
```
