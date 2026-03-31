# Slot: isDevelopedBy

_Indicates the developer of an AI system or component._

URI: [airo:isDevelopedBy](https://w3id.org/airo#isDevelopedBy)
Alias: isDevelopedBy

<!-- no inheritance hierarchy -->

## Applicable Classes

| Name                    | Description                                                                      | Modifies Slot |
| ----------------------- | -------------------------------------------------------------------------------- | ------------- |
| [AiAgent](AiAgent.md)   | An artificial intelligence (AI) agent refers to a system or program that is c... | no            |
| [AiSystem](AiSystem.md) | A compound AI System composed of one or more AI capablities                      | no            |

## Properties

- Range: [AIDeveloper](AIDeveloper.md)

## Identifier and Mapping Information

### Schema Source

- from schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology

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
from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
rank: 1000
domain: '[''AISystem'', ''AIComponent'']'
slot_uri: airo:isDevelopedBy
alias: isDevelopedBy
domain_of:
- AiSystem
range: AIDeveloper

```
</details>
```
