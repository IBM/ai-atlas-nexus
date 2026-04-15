# Slot: hasAIUser

_Indicate the end-user of an AI system._

URI: [airo:hasAiUser](https://w3id.org/airo#hasAiUser)
Alias: hasAIUser

<!-- no inheritance hierarchy -->

## Applicable Classes

| Name                    | Description                                                                      | Modifies Slot |
| ----------------------- | -------------------------------------------------------------------------------- | ------------- |
| [AiAgent](AiAgent.md)   | An artificial intelligence (AI) agent refers to a system or program that is c... | no            |
| [AiSystem](AiSystem.md) | A compound AI System composed of one or more AI capablities                      | no            |

## Properties

- Range: [String](String.md)

## Identifier and Mapping Information

### Schema Source

- from schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology

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
from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
rank: 1000
domain: AISystem
slot_uri: airo:hasAiUser
alias: hasAIUser
domain_of:
- AiSystem
range: string

```
</details>
```
