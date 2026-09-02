---
search:
  boost: 5.0
---

# Slot: hasAIUser

_Indicate the end-user of an AI system._

<div data-search-exclude markdown="1">

URI: [airo:hasAiUser](https://w3id.org/airo#hasAiUser)
Alias: hasAIUser

<!-- no inheritance hierarchy -->

## Applicable Classes

| Name                    | Description                                                                      | Modifies Slot |
| ----------------------- | -------------------------------------------------------------------------------- | ------------- |
| [AiAgent](AiAgent.md)   | An artificial intelligence (AI) agent refers to a system or program that is c... | no            |
| [AiSystem](AiSystem.md) | A compound AI System composed of one or more AI capablities                      | no            |

## Properties

### Type and Range

| Property  | Value                                             |
| --------- | ------------------------------------------------- |
| Range     | [AIUser](AIUser.md)                               |
| Domain    | [AiSystem](AiSystem.md)                           |
| Domain Of | [AiSystem](AiSystem.md)                           |
| Slot URI  | [airo:hasAiUser](https://w3id.org/airo#hasAiUser) |

### Cardinality and Requirements

| Property    | Value |
| ----------- | ----- |
| Multivalued | Yes   |

## Identifier and Mapping Information

### Schema Source

- from schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology

## Mappings

| Mapping Type | Mapped Value    |
| ------------ | --------------- |
| self         | airo:hasAiUser  |
| native       | nexus:hasAIUser |

## LinkML Source

<details>
```yaml
name: hasAIUser
description: Indicate the end-user of an AI system.
from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
rank: 1000
domain: AiSystem
slot_uri: airo:hasAiUser
alias: hasAIUser
domain_of:
- AiSystem
range: AIUser
multivalued: true

```
</details></div>
```
