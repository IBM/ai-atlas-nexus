---
search:
  boost: 5.0
---

# Slot: hasStandardConformance

_The completed checklist(s) of evaluation standards (e.g. AEF-1) that the engagement reports against._

<div data-search-exclude markdown="1">

URI: [nexus:hasStandardConformance](https://w3id.org/ai-atlas-nexus/hasStandardConformance)

<!-- no inheritance hierarchy -->

## Applicable Classes

| Name                                                                | Description                                                                      | Modifies Slot |
| ------------------------------------------------------------------- | -------------------------------------------------------------------------------- | ------------- |
| [ThirdPartyEvaluationEngagement](ThirdPartyEvaluationEngagement.md) | A single engagement in which an independent third-party evaluator evaluates o... | no            |

## Properties

### Type and Range

| Property  | Value                                                                                  |
| --------- | -------------------------------------------------------------------------------------- |
| Range     | [EvaluationStandardConformance](EvaluationStandardConformance.md)                      |
| Domain Of | [ThirdPartyEvaluationEngagement](ThirdPartyEvaluationEngagement.md)                    |
| Slot URI  | [nexus:hasStandardConformance](https://w3id.org/ai-atlas-nexus/hasStandardConformance) |

### Cardinality and Requirements

| Property    | Value |
| ----------- | ----- |
| Multivalued | Yes   |

## Identifier and Mapping Information

### Schema Source

- from schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology

## Mappings

| Mapping Type | Mapped Value                 |
| ------------ | ---------------------------- |
| self         | nexus:hasStandardConformance |
| native       | nexus:hasStandardConformance |

## LinkML Source

<details>
```yaml
name: hasStandardConformance
description: The completed checklist(s) of evaluation standards (e.g. AEF-1) that
  the engagement reports against.
from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
rank: 1000
slot_uri: nexus:hasStandardConformance
domain_of:
- ThirdPartyEvaluationEngagement
range: EvaluationStandardConformance
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>
```
