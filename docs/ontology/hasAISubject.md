# Slot: hasAISubject

_Indicates the subjects of an AI system_

URI: [airo:hasAISubject](https://w3id.org/airo#hasAISubject)
Alias: hasAISubject

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

| Property | Value |
| -------- | ----- |

## Identifier and Mapping Information

### Schema Source

- from schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology

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
from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
rank: 1000
slot_uri: airo:hasAISubject
alias: hasAISubject
domain_of:
- AiSystem
range: AISubject

```
</details>
```
