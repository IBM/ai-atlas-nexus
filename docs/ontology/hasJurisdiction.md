---
search:
  boost: 5.0
---

# Slot: hasJurisdiction

_The legal or political jurisdiction(s) in which this concept applies, expressed as ISO 3166-1 country codes._

<div data-search-exclude markdown="1">

URI: [dpv:hasJurisdiction](https://w3id.org/dpv#hasJurisdiction)
Alias: hasJurisdiction

<!-- no inheritance hierarchy -->

## Applicable Classes

| Name                                      | Description                                                                      | Modifies Slot |
| ----------------------------------------- | -------------------------------------------------------------------------------- | ------------- |
| [Risk](Risk.md)                           | The state of uncertainty associated with an AI system, that has the potential... | no            |
| [Capability](Capability.md)               | A specific AI capability or ability, such as reading comprehension, logical r... | no            |
| [RiskControlGroup](RiskControlGroup.md)   | A group of AI system related risk controls                                       | no            |
| [RiskGroup](RiskGroup.md)                 | A group of AI system related risks that are part of a risk taxonomy              | no            |
| [RiskControl](RiskControl.md)             | A measure that maintains and/or modifies risk (and risk concepts)                | no            |
| [RiskConcept](RiskConcept.md)             | An umbrella term for referring to risk, risk source, consequence and impact      | no            |
| [CapabilityConcept](CapabilityConcept.md) | An umbrella term for referring to capability domains, groups, and individual ... | no            |
| [CapabilityDomain](CapabilityDomain.md)   | A high-level domain of AI capabilities (e                                        | no            |
| [RiskIncident](RiskIncident.md)           | An event occuring or occured which is a realised or materialised risk            | no            |
| [Concept](Concept.md)                     | A concept                                                                        | no            |
| [Action](Action.md)                       | Action to remediate a risk                                                       | no            |
| [Impact](Impact.md)                       |                                                                                  | no            |
| [CapabilityGroup](CapabilityGroup.md)     | A group of AI capabilities that are part of a capability taxonomy, organized ... | no            |

## Properties

### Type and Range

| Property  | Value                                                       |
| --------- | ----------------------------------------------------------- |
| Range     | [Jurisdiction](Jurisdiction.md)                             |
| Domain Of | [Concept](Concept.md)                                       |
| Slot URI  | [dpv:hasJurisdiction](https://w3id.org/dpv#hasJurisdiction) |

### Cardinality and Requirements

| Property    | Value |
| ----------- | ----- |
| Multivalued | Yes   |

## Identifier and Mapping Information

### Schema Source

- from schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology

## Mappings

| Mapping Type | Mapped Value          |
| ------------ | --------------------- |
| self         | dpv:hasJurisdiction   |
| native       | nexus:hasJurisdiction |

## LinkML Source

<details>
```yaml
name: hasJurisdiction
description: The legal or political jurisdiction(s) in which this concept applies,
  expressed as ISO 3166-1 country codes.
from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
rank: 1000
slot_uri: dpv:hasJurisdiction
alias: hasJurisdiction
domain_of:
- Concept
range: Jurisdiction
multivalued: true
inlined: false

```
</details></div>
```
