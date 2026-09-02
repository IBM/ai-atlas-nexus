---
search:
  boost: 5.0
---

# Slot: hasJurisdiction

_The legal or regulatory jurisdiction(s) applicable to an AI system, policy, risk, or obligation. Accepts ISO 3166-1 country codes, supra-national bodies, or subnational jurisdictions with distinct regulatory significance. Aligns with dpv:hasJurisdiction._

<div data-search-exclude markdown="1">

URI: [dpv:hasJurisdiction](https://w3id.org/dpv#hasJurisdiction)
Alias: hasJurisdiction

<!-- no inheritance hierarchy -->

## Applicable Classes

| Name                                      | Description                                                                      | Modifies Slot |
| ----------------------------------------- | -------------------------------------------------------------------------------- | ------------- |
| [Capability](Capability.md)               | A specific AI capability or ability, such as reading comprehension, logical r... | no            |
| [Action](Action.md)                       | Action to remediate a risk                                                       | no            |
| [RiskConcept](RiskConcept.md)             | An umbrella term for referring to risk, risk source, consequence and impact      | no            |
| [Concept](Concept.md)                     | A concept                                                                        | no            |
| [CapabilityGroup](CapabilityGroup.md)     | A group of AI capabilities that are part of a capability taxonomy, organized ... | no            |
| [Impact](Impact.md)                       |                                                                                  | no            |
| [Risk](Risk.md)                           | The state of uncertainty associated with an AI system, that has the potential... | no            |
| [CapabilityDomain](CapabilityDomain.md)   | A high-level domain of AI capabilities (e                                        | no            |
| [RiskIncident](RiskIncident.md)           | An event occuring or occured which is a realised or materialised risk            | no            |
| [CapabilityConcept](CapabilityConcept.md) | An umbrella term for referring to capability domains, groups, and individual ... | no            |
| [RiskGroup](RiskGroup.md)                 | A group of AI system related risks that are part of a risk taxonomy              | no            |
| [RiskControlGroup](RiskControlGroup.md)   | A group of AI system related risk controls                                       | no            |
| [RiskControl](RiskControl.md)             | A measure that maintains and/or modifies risk (and risk concepts)                | no            |

## Properties

### Type and Range

| Property  | Value                                                                                                                                                                                                                        |
| --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Range     | [Jurisdiction](Jurisdiction.md)&nbsp;or&nbsp;<br />[String](String.md)&nbsp;or&nbsp;<br />[SubnationalJurisdiction](SubnationalJurisdiction.md)&nbsp;or&nbsp;<br />[SupraNationalJurisdiction](SupraNationalJurisdiction.md) |
| Domain Of | [Concept](Concept.md)                                                                                                                                                                                                        |
| Slot URI  | [dpv:hasJurisdiction](https://w3id.org/dpv#hasJurisdiction)                                                                                                                                                                  |

### Cardinality and Requirements

| Property    | Value |
| ----------- | ----- |
| Multivalued | Yes   |

<details>
<summary>Expressions & Logic</summary>
#### Any Of

Value must satisfy at least one of:

- AnonymousSlotExpression({'range': 'Jurisdiction'})
- AnonymousSlotExpression({'range': 'SupraNationalJurisdiction'})
- AnonymousSlotExpression({'range': 'SubnationalJurisdiction'})

</details>

## See Also

- [https://w3id.org/dpv#hasJurisdiction](https://w3id.org/dpv#hasJurisdiction)

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
description: The legal or regulatory jurisdiction(s) applicable to an AI system, policy,
  risk, or obligation. Accepts ISO 3166-1 country codes, supra-national bodies, or
  subnational jurisdictions with distinct regulatory significance. Aligns with dpv:hasJurisdiction.
from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
see_also:
- https://w3id.org/dpv#hasJurisdiction
rank: 1000
slot_uri: dpv:hasJurisdiction
alias: hasJurisdiction
domain_of:
- Concept
range: string
multivalued: true
inlined: false
any_of:
- range: Jurisdiction
- range: SupraNationalJurisdiction
- range: SubnationalJurisdiction

```
</details></div>
```
