---
search:
  boost: 5.0
---

# Slot: isDetectedBy

_A relationship where a risk, risk source, consequence, or impact is detected by a risk control._

<div data-search-exclude markdown="1">

URI: [nexus:isDetectedBy](https://w3id.org/ai-atlas-nexus/isDetectedBy)
Alias: isDetectedBy

<!-- no inheritance hierarchy -->

## Applicable Classes

| Name                                    | Description                                                                      | Modifies Slot |
| --------------------------------------- | -------------------------------------------------------------------------------- | ------------- |
| [Action](Action.md)                     | Action to remediate a risk                                                       | no            |
| [RiskConcept](RiskConcept.md)           | An umbrella term for referring to risk, risk source, consequence and impact      | no            |
| [Impact](Impact.md)                     |                                                                                  | no            |
| [Risk](Risk.md)                         | The state of uncertainty associated with an AI system, that has the potential... | no            |
| [RiskIncident](RiskIncident.md)         | An event occuring or occured which is a realised or materialised risk            | no            |
| [RiskGroup](RiskGroup.md)               | A group of AI system related risks that are part of a risk taxonomy              | no            |
| [RiskControlGroup](RiskControlGroup.md) | A group of AI system related risk controls                                       | no            |
| [RiskControl](RiskControl.md)           | A measure that maintains and/or modifies risk (and risk concepts)                | no            |

## Properties

### Type and Range

| Property  | Value                         |
| --------- | ----------------------------- |
| Range     | [RiskControl](RiskControl.md) |
| Domain    | [RiskConcept](RiskConcept.md) |
| Domain Of | [RiskConcept](RiskConcept.md) |

### Cardinality and Requirements

| Property    | Value |
| ----------- | ----- |
| Multivalued | Yes   |

<details>
<summary>Relationship Properties</summary>

| Property | Value                                       |
| -------- | ------------------------------------------- |
| Inverse  | [detectsRiskConcept](detectsRiskConcept.md) |

</details>

## Identifier and Mapping Information

### Schema Source

- from schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology

## Mappings

| Mapping Type | Mapped Value       |
| ------------ | ------------------ |
| self         | nexus:isDetectedBy |
| native       | nexus:isDetectedBy |

## LinkML Source

<details>
```yaml
name: isDetectedBy
description: A relationship where a risk, risk source, consequence, or impact is detected
  by a risk control.
from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
rank: 1000
domain: RiskConcept
alias: isDetectedBy
domain_of:
- RiskConcept
inverse: detectsRiskConcept
range: RiskControl
multivalued: true
inlined: false

```
</details></div>
```
