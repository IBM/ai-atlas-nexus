---
search:
  boost: 5.0
---

# Slot: isDevelopedBy

_Indicates the developer of an AI system or component._

<div data-search-exclude markdown="1">

URI: [airo:isDevelopedBy](https://w3id.org/airo#isDevelopedBy)

<!-- no inheritance hierarchy -->

## Applicable Classes

| Name                    | Description                                                                      | Modifies Slot |
| ----------------------- | -------------------------------------------------------------------------------- | ------------- |
| [AiSystem](AiSystem.md) | A compound AI System composed of one or more AI capablities                      | no            |
| [AiAgent](AiAgent.md)   | An artificial intelligence (AI) agent refers to a system or program that is c... | no            |

## Properties

### Type and Range

| Property  | Value                                                     |
| --------- | --------------------------------------------------------- |
| Range     | [AIDeveloper](AIDeveloper.md)                             |
| Domain Of | [AiSystem](AiSystem.md)                                   |
| Slot URI  | [airo:isDevelopedBy](https://w3id.org/airo#isDevelopedBy) |

### Cardinality and Requirements

| Property | Value |
| -------- | ----- |

## Identifier and Mapping Information

### Schema Source

- from schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology

## Mappings

| Mapping Type | Mapped Value        |
| ------------ | ------------------- |
| self         | airo:isDevelopedBy  |
| native       | nexus:isDevelopedBy |

## LinkML Source

<details>
```yaml
name: isDevelopedBy
description: Indicates the developer of an AI system or component.
from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
rank: 1000
slot_uri: airo:isDevelopedBy
domain_of:
- AiSystem
range: AIDeveloper

```
</details></div>
```
