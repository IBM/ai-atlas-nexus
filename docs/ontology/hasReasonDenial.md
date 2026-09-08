---
search:
  boost: 5.0
---

# Slot: hasReasonDenial

_Reason for denial_

<div data-search-exclude markdown="1">

URI: [nexus:hasReasonDenial](https://w3id.org/ai-atlas-nexus/hasReasonDenial)

<!-- no inheritance hierarchy -->

## Applicable Classes

| Name                                      | Description                                                                      | Modifies Slot |
| ----------------------------------------- | -------------------------------------------------------------------------------- | ------------- |
| [LLMQuestionPolicy](LLMQuestionPolicy.md) | The policy guides how the language model should answer a diverse set of sensi... | no            |

## Properties

### Type and Range

| Property  | Value                                                                    |
| --------- | ------------------------------------------------------------------------ |
| Range     | [String](String.md)                                                      |
| Domain Of | [LLMQuestionPolicy](LLMQuestionPolicy.md)                                |
| Slot URI  | [nexus:hasReasonDenial](https://w3id.org/ai-atlas-nexus/hasReasonDenial) |

### Cardinality and Requirements

| Property | Value |
| -------- | ----- |

## Identifier and Mapping Information

### Schema Source

- from schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology

## Mappings

| Mapping Type | Mapped Value          |
| ------------ | --------------------- |
| self         | nexus:hasReasonDenial |
| native       | nexus:hasReasonDenial |

## LinkML Source

<details>
```yaml
name: hasReasonDenial
description: Reason for denial
from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
rank: 1000
slot_uri: nexus:hasReasonDenial
domain_of:
- LLMQuestionPolicy
range: string
multivalued: false
inlined: true

```
</details></div>
```
