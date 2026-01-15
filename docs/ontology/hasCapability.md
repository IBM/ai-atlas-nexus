

# Slot: hasCapability


_Indicates the technical capabilities this entry possesses._

__





URI: [tech:hasCapability](https://w3id.org/dpv/tech#hasCapability)
Alias: hasCapability

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AiAgent](AiAgent.md) | An artificial intelligence (AI) agent refers to a system or program that is c... |  no  |
| [LLMIntrinsic](LLMIntrinsic.md) | A capability that can be invoked through a well-defined API that is reasonabl... |  no  |
| [AiSystem](AiSystem.md) | A compound AI System composed of one or more AI capablities |  no  |
| [Adapter](Adapter.md) | Adapter-based methods add extra trainable parameters after the attention and ... |  no  |






## Properties

* Range: [Capability](Capability.md)

* Multivalued: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tech:hasCapability |
| native | nexus:hasCapability |




## LinkML Source

<details>
```yaml
name: hasCapability
description: 'Indicates the technical capabilities this entry possesses.

  '
from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
rank: 1000
slot_uri: tech:hasCapability
alias: hasCapability
domain_of:
- AiSystem
- Adapter
- LLMIntrinsic
range: Capability
multivalued: true
inlined: false

```
</details>
