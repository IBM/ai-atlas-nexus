---
search:
  boost: 5.0
---

# Slot: hasException

_Exception type_

<div data-search-exclude markdown="1">

URI: [nexus:hasException](https://w3id.org/ai-atlas-nexus/hasException)

<!-- no inheritance hierarchy -->

## Applicable Classes

| Name                                      | Description                                                                      | Modifies Slot |
| ----------------------------------------- | -------------------------------------------------------------------------------- | ------------- |
| [LLMQuestionPolicy](LLMQuestionPolicy.md) | The policy guides how the language model should answer a diverse set of sensi... | no            |

## Properties

### Type and Range

| Property  | Value                                                              |
| --------- | ------------------------------------------------------------------ |
| Range     | [String](String.md)                                                |
| Domain Of | [LLMQuestionPolicy](LLMQuestionPolicy.md)                          |
| Slot URI  | [nexus:hasException](https://w3id.org/ai-atlas-nexus/hasException) |

### Cardinality and Requirements

| Property | Value |
| -------- | ----- |

## Identifier and Mapping Information

### Schema Source

- from schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology

## Mappings

| Mapping Type | Mapped Value       |
| ------------ | ------------------ |
| self         | nexus:hasException |
| native       | nexus:hasException |

## LinkML Source

<details>
```yaml
name: hasException
description: Exception type
from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
rank: 1000
slot_uri: nexus:hasException
domain_of:
- LLMQuestionPolicy
range: string
multivalued: false
inlined: true

```
</details></div>
```
