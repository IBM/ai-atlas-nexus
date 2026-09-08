---
search:
  boost: 5.0
---

# Slot: isMitigatedBy

_A relationship where a risk, risk source, consequence, or impact is mitigated by a risk control._

<div data-search-exclude markdown="1">

URI: [nexus:isMitigatedBy](https://w3id.org/ai-atlas-nexus/isMitigatedBy)

<!-- no inheritance hierarchy -->

## Applicable Classes

| Name                                    | Description                                                                      | Modifies Slot |
| --------------------------------------- | -------------------------------------------------------------------------------- | ------------- |
| [RiskConcept](RiskConcept.md)           | An umbrella term for referring to risk, risk source, consequence and impact      | no            |
| [RiskControlGroup](RiskControlGroup.md) | A group of AI system related risk controls                                       | no            |
| [RiskGroup](RiskGroup.md)               | A group of AI system related risks that are part of a risk taxonomy              | no            |
| [Risk](Risk.md)                         | The state of uncertainty associated with an AI system, that has the potential... | no            |
| [RiskControl](RiskControl.md)           | A measure that maintains and/or modifies risk (and risk concepts)                | no            |
| [Action](Action.md)                     | Action to remediate a risk                                                       | no            |
| [RiskIncident](RiskIncident.md)         | An event occuring or occured which is a realised or materialised risk            | no            |
| [Impact](Impact.md)                     |                                                                                  | no            |

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

| Property | Value                                           |
| -------- | ----------------------------------------------- |
| Inverse  | [mitigatesRiskConcept](mitigatesRiskConcept.md) |

</details>

## Identifier and Mapping Information

### Schema Source

- from schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology

## Mappings

| Mapping Type | Mapped Value        |
| ------------ | ------------------- |
| self         | nexus:isMitigatedBy |
| native       | nexus:isMitigatedBy |

## LinkML Source

<details>
```yaml
name: isMitigatedBy
description: A relationship where a risk, risk source, consequence, or impact is mitigated
  by a risk control.
from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
rank: 1000
domain: RiskConcept
domain_of:
- RiskConcept
inverse: mitigatesRiskConcept
range: RiskControl
multivalued: true
inlined: false

```
</details></div>
```
