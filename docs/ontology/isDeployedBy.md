---
search:
  boost: 5.0
---

# Slot: isDeployedBy

_Indicates the deployer of an AI system or component._

<div data-search-exclude markdown="1">

URI: [airo:isDeployedBy](https://w3id.org/airo#isDeployedBy)

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
| Range     | [AIDeployer](AIDeployer.md)                             |
| Domain Of | [AiSystem](AiSystem.md)                                 |
| Slot URI  | [airo:isDeployedBy](https://w3id.org/airo#isDeployedBy) |

### Cardinality and Requirements

| Property | Value |
| -------- | ----- |

## Identifier and Mapping Information

### Schema Source

- from schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology

## Mappings

| Mapping Type | Mapped Value       |
| ------------ | ------------------ |
| self         | airo:isDeployedBy  |
| native       | nexus:isDeployedBy |

## LinkML Source

<details>
```yaml
name: isDeployedBy
description: Indicates the deployer of an AI system or component.
from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
rank: 1000
slot_uri: airo:isDeployedBy
domain_of:
- AiSystem
range: AIDeployer

```
</details></div>
```
