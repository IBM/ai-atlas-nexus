---
search:
  boost: 5.0
---

# Slot: hasEuRiskCategory

_The risk category of an AI system as defined by the EU AI Act._

<div data-search-exclude markdown="1">

URI: [nexus:hasEuRiskCategory](https://w3id.org/ai-atlas-nexus/hasEuRiskCategory)
Alias: hasEuRiskCategory

<!-- no inheritance hierarchy -->

## Applicable Classes

| Name                    | Description                                                                      | Modifies Slot |
| ----------------------- | -------------------------------------------------------------------------------- | ------------- |
| [AiAgent](AiAgent.md)   | An artificial intelligence (AI) agent refers to a system or program that is c... | no            |
| [AiSystem](AiSystem.md) | A compound AI System composed of one or more AI capablities                      | no            |

## Properties

### Type and Range

| Property  | Value                                   |
| --------- | --------------------------------------- |
| Range     | [EuAiRiskCategory](EuAiRiskCategory.md) |
| Domain Of | [AiSystem](AiSystem.md)                 |

### Cardinality and Requirements

| Property | Value |
| -------- | ----- |

## Identifier and Mapping Information

### Schema Source

- from schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology

## Mappings

| Mapping Type | Mapped Value            |
| ------------ | ----------------------- |
| self         | nexus:hasEuRiskCategory |
| native       | nexus:hasEuRiskCategory |

## LinkML Source

<details>
```yaml
name: hasEuRiskCategory
description: The risk category of an AI system as defined by the EU AI Act.
from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
rank: 1000
alias: hasEuRiskCategory
domain_of:
- AiSystem
range: EuAiRiskCategory

```
</details></div>
```
