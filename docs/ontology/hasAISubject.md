---
search:
  boost: 5.0
---

# Slot: hasAISubject

_Indicates the subjects of an AI system_

<div data-search-exclude markdown="1">

URI: [airo:hasAISubject](https://w3id.org/airo#hasAISubject)

<!-- no inheritance hierarchy -->

## Applicable Classes

| Name                    | Description                                                                      | Modifies Slot |
| ----------------------- | -------------------------------------------------------------------------------- | ------------- |
| [AiSystem](AiSystem.md) | A compound AI System composed of one or more AI capablities                      | no            |
| [AiAgent](AiAgent.md)   | An artificial intelligence (AI) agent refers to a system or program that is c... | no            |

## Properties

### Type and Range

| Property  | Value                                                   |
| --------- | ------------------------------------------------------- |
| Range     | [AISubject](AISubject.md)                               |
| Domain Of | [AiSystem](AiSystem.md)                                 |
| Slot URI  | [airo:hasAISubject](https://w3id.org/airo#hasAISubject) |

### Cardinality and Requirements

| Property    | Value |
| ----------- | ----- |
| Multivalued | Yes   |

## Identifier and Mapping Information

### Schema Source

- from schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology

## Mappings

| Mapping Type | Mapped Value       |
| ------------ | ------------------ |
| self         | airo:hasAISubject  |
| native       | nexus:hasAISubject |

## LinkML Source

<details>
```yaml
name: hasAISubject
description: Indicates the subjects of an AI system
from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
rank: 1000
slot_uri: airo:hasAISubject
domain_of:
- AiSystem
range: AISubject
multivalued: true

```
</details></div>
```
