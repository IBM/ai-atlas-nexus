---
search:
  boost: 5.0
---

# Slot: conformsToStandard

_The evaluation standard the checklist is completed against._

<div data-search-exclude markdown="1">

URI: [dcterms:conformsTo](http://purl.org/dc/terms/conformsTo)

<!-- no inheritance hierarchy -->

## Applicable Classes

| Name                                                              | Description                                                                      | Modifies Slot |
| ----------------------------------------------------------------- | -------------------------------------------------------------------------------- | ------------- |
| [EvaluationStandardConformance](EvaluationStandardConformance.md) | A completed checklist reporting how an engagement addressed the conditions of... | yes           |

## Properties

### Type and Range

| Property  | Value                                                             |
| --------- | ----------------------------------------------------------------- |
| Range     | [EvaluationStandard](EvaluationStandard.md)                       |
| Domain Of | [EvaluationStandardConformance](EvaluationStandardConformance.md) |
| Slot URI  | [dcterms:conformsTo](http://purl.org/dc/terms/conformsTo)         |

### Cardinality and Requirements

| Property | Value |
| -------- | ----- |

## Identifier and Mapping Information

### Schema Source

- from schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology

## Mappings

| Mapping Type | Mapped Value             |
| ------------ | ------------------------ |
| self         | dcterms:conformsTo       |
| native       | nexus:conformsToStandard |

## LinkML Source

<details>
```yaml
name: conformsToStandard
description: The evaluation standard the checklist is completed against.
from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
rank: 1000
slot_uri: dcterms:conformsTo
domain_of:
- EvaluationStandardConformance
range: EvaluationStandard
inlined: false

```
</details></div>
```
