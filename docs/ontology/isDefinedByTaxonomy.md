

# Slot: isDefinedByTaxonomy


_A relationship where a concept or a concept group is defined by a taxonomy_





URI: [schema:isPartOf](http://schema.org/isPartOf)
Alias: isDefinedByTaxonomy

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [CapabilityDomain](CapabilityDomain.md) | A high-level domain of AI capabilities (e |  no  |
| [CapabilityGroup](CapabilityGroup.md) | A group of AI capabilities that are part of a capability taxonomy, organized ... |  no  |
| [StakeholderGroup](StakeholderGroup.md) | An AI system stakeholder grouping |  no  |
| [Term](Term.md) | A term and its definitions |  no  |
| [Risk](Risk.md) | The state of uncertainty associated with an AI system, that has the potential... |  no  |
| [Capability](Capability.md) | A specific AI capability or ability, such as reading comprehension, logical r... |  no  |
| [LLMIntrinsic](LLMIntrinsic.md) | A capability that can be invoked through a well-defined API that is reasonabl... |  no  |
| [RiskIncident](RiskIncident.md) | An event occuring or occured which is a realised or materialised risk |  no  |
| [Concept](Concept.md) | A concept |  no  |
| [Control](Control.md) | A measure that maintains and/or modifies |  no  |
| [Group](Group.md) | Labelled groups of concepts |  no  |
| [LLMQuestionPolicy](LLMQuestionPolicy.md) | The policy guides how the language model should answer a diverse set of sensi... |  no  |
| [Impact](Impact.md) |  |  no  |
| [Adapter](Adapter.md) | Adapter-based methods add extra trainable parameters after the attention and ... |  no  |
| [Principle](Principle.md) | A representation of values or norms that must be taken into consideration whe... |  no  |
| [Stakeholder](Stakeholder.md) | An AI system stakeholder for Responsible AI governance (e |  no  |
| [Action](Action.md) | Action to remediate a risk |  no  |
| [CapabilityConcept](CapabilityConcept.md) | An umbrella term for referring to capability domains, groups, and individual ... |  no  |
| [Policy](Policy.md) | A guidance document outlining any of: procedures, plans, principles, decision... |  no  |
| [Entry](Entry.md) | An entry and its definitions |  no  |
| [AiTask](AiTask.md) | A task, such as summarization and classification, performed by an AI |  no  |
| [RiskGroup](RiskGroup.md) | A group of AI system related risks that are part of a risk taxonomy |  no  |
| [RiskControl](RiskControl.md) | A measure that maintains and/or modifies risk (and risk concepts) |  no  |
| [RiskConcept](RiskConcept.md) | An umbrella term for referring to risk, risk source, consequence and impact |  no  |






## Properties

* Range: [Taxonomy](Taxonomy.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | schema:isPartOf |
| native | nexus:isDefinedByTaxonomy |




## LinkML Source

<details>
```yaml
name: isDefinedByTaxonomy
description: A relationship where a concept or a concept group is defined by a taxonomy
from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
rank: 1000
slot_uri: schema:isPartOf
alias: isDefinedByTaxonomy
domain_of:
- Concept
- Control
- Group
- Entry
- Policy
- RiskGroup
- Risk
- RiskControl
- Action
- RiskIncident
- CapabilityGroup
- StakeholderGroup
- Stakeholder
range: Taxonomy

```
</details>
