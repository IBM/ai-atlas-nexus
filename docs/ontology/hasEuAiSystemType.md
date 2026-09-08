---
search:
  boost: 5.0
---

# Slot: hasEuAiSystemType

_The type of system as defined by the EU AI Act._

<div data-search-exclude markdown="1">

URI: [nexus:hasEuAiSystemType](https://w3id.org/ai-atlas-nexus/hasEuAiSystemType)

<!-- no inheritance hierarchy -->

## Applicable Classes

| Name                    | Description                                                                      | Modifies Slot |
| ----------------------- | -------------------------------------------------------------------------------- | ------------- |
| [AiSystem](AiSystem.md) | A compound AI System composed of one or more AI capablities                      | no            |
| [AiAgent](AiAgent.md)   | An artificial intelligence (AI) agent refers to a system or program that is c... | no            |

## Properties

### Type and Range

| Property  | Value                           |
| --------- | ------------------------------- |
| Range     | [AiSystemType](AiSystemType.md) |
| Domain Of | [AiSystem](AiSystem.md)         |

### Cardinality and Requirements

| Property | Value |
| -------- | ----- |

## Identifier and Mapping Information

### Schema Source

- from schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology

## Mappings

| Mapping Type | Mapped Value            |
| ------------ | ----------------------- |
| self         | nexus:hasEuAiSystemType |
| native       | nexus:hasEuAiSystemType |

## LinkML Source

<details>
```yaml
name: hasEuAiSystemType
description: The type of system as defined by the EU AI Act.
from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
rank: 1000
domain_of:
- AiSystem
range: AiSystemType

```
</details></div>
```
