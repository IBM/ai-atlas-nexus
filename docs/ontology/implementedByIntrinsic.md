

# Slot: implementedByIntrinsic


_Indicates that this capability is implemented by a specific LLM intrinsic. This relationship distinguishes the abstract capability (what can be done) from the technical implementation mechanism (how it is done at the model component level)._





URI: [nexus:implementedByIntrinsic](https://ibm.github.io/ai-atlas-nexus/ontology/implementedByIntrinsic)
Alias: implementedByIntrinsic

<!-- no inheritance hierarchy -->







## Properties

* Range: [LLMIntrinsic](LLMIntrinsic.md)

* Multivalued: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | nexus:implementedByIntrinsic |
| native | nexus:implementedByIntrinsic |




## LinkML Source

<details>
```yaml
name: implementedByIntrinsic
description: Indicates that this capability is implemented by a specific LLM intrinsic.
  This relationship distinguishes the abstract capability (what can be done) from
  the technical implementation mechanism (how it is done at the model component level).
from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
rank: 1000
alias: implementedByIntrinsic
inverse: implementsCapability
range: LLMIntrinsic
multivalued: true
inlined: false

```
</details>
