---
search:
  boost: 5.0
---

# Slot: isUsedWithinLocality

_Specifies the domain an AI system is used within._

<div data-search-exclude markdown="1">

URI: [airo:isUsedWithinLocality](https://w3id.org/airo#isUsedWithinLocality)

<!-- no inheritance hierarchy -->

## Applicable Classes

| Name                                    | Description                                                                      | Modifies Slot |
| --------------------------------------- | -------------------------------------------------------------------------------- | ------------- |
| [RiskConcept](RiskConcept.md)           | An umbrella term for referring to risk, risk source, consequence and impact      | no            |
| [AiSystem](AiSystem.md)                 | A compound AI System composed of one or more AI capablities                      | no            |
| [RiskControlGroup](RiskControlGroup.md) | A group of AI system related risk controls                                       | no            |
| [RiskGroup](RiskGroup.md)               | A group of AI system related risks that are part of a risk taxonomy              | no            |
| [Risk](Risk.md)                         | The state of uncertainty associated with an AI system, that has the potential... | no            |
| [RiskControl](RiskControl.md)           | A measure that maintains and/or modifies risk (and risk concepts)                | no            |
| [Action](Action.md)                     | Action to remediate a risk                                                       | no            |
| [RiskIncident](RiskIncident.md)         | An event occuring or occured which is a realised or materialised risk            | no            |
| [Impact](Impact.md)                     |                                                                                  | no            |
| [AiAgent](AiAgent.md)                   | An artificial intelligence (AI) agent refers to a system or program that is c... | no            |

## Properties

### Type and Range

| Property  | Value                                                                   |
| --------- | ----------------------------------------------------------------------- |
| Range     | [LocalityOfUse](LocalityOfUse.md)                                       |
| Domain Of | [RiskConcept](RiskConcept.md), [AiSystem](AiSystem.md)                  |
| Slot URI  | [airo:isUsedWithinLocality](https://w3id.org/airo#isUsedWithinLocality) |

### Cardinality and Requirements

| Property    | Value |
| ----------- | ----- |
| Multivalued | Yes   |

## Identifier and Mapping Information

### Schema Source

- from schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology

## Mappings

| Mapping Type | Mapped Value               |
| ------------ | -------------------------- |
| self         | airo:isUsedWithinLocality  |
| native       | nexus:isUsedWithinLocality |

## LinkML Source

<details>
```yaml
name: isUsedWithinLocality
description: Specifies the domain an AI system is used within.
from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
rank: 1000
slot_uri: airo:isUsedWithinLocality
domain_of:
- RiskConcept
- AiSystem
range: LocalityOfUse
multivalued: true
inlined: false

```
</details></div>
```
