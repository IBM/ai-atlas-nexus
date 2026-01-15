

# Class: LLMIntrinsic


_A capability that can be invoked through a well-defined API that is reasonably stable and independent of how the LLM intrinsic itself is implemented._





URI: [ai:Capability](https://w3id.org/dpv/ai#Capability)





```mermaid
 classDiagram
    class LLMIntrinsic
    click LLMIntrinsic href "../LLMIntrinsic/"
      Entry <|-- LLMIntrinsic
        click Entry href "../Entry/"

      LLMIntrinsic : broad_mappings





        LLMIntrinsic --> "*" Any : broad_mappings
        click Any href "../Any/"



      LLMIntrinsic : close_mappings





        LLMIntrinsic --> "*" Any : close_mappings
        click Any href "../Any/"



      LLMIntrinsic : dateCreated

      LLMIntrinsic : dateModified

      LLMIntrinsic : description

      LLMIntrinsic : exact_mappings





        LLMIntrinsic --> "*" Any : exact_mappings
        click Any href "../Any/"



      LLMIntrinsic : hasAdapter





        LLMIntrinsic --> "*" Adapter : hasAdapter
        click Adapter href "../Adapter/"



      LLMIntrinsic : hasCapability





        LLMIntrinsic --> "*" Capability : hasCapability
        click Capability href "../Capability/"



      LLMIntrinsic : hasDocumentation





        LLMIntrinsic --> "*" Documentation : hasDocumentation
        click Documentation href "../Documentation/"



      LLMIntrinsic : hasRelatedRisk





        LLMIntrinsic --> "*" Risk : hasRelatedRisk
        click Risk href "../Risk/"



      LLMIntrinsic : hasRelatedTerm





        LLMIntrinsic --> "*" Term : hasRelatedTerm
        click Term href "../Term/"



      LLMIntrinsic : id

      LLMIntrinsic : implementedByAdapter





        LLMIntrinsic --> "*" Adapter : implementedByAdapter
        click Adapter href "../Adapter/"



      LLMIntrinsic : isDefinedByTaxonomy





        LLMIntrinsic --> "0..1" Taxonomy : isDefinedByTaxonomy
        click Taxonomy href "../Taxonomy/"



      LLMIntrinsic : isDefinedByVocabulary





        LLMIntrinsic --> "0..1" Vocabulary : isDefinedByVocabulary
        click Vocabulary href "../Vocabulary/"



      LLMIntrinsic : isPartOf

      LLMIntrinsic : name

      LLMIntrinsic : narrow_mappings





        LLMIntrinsic --> "*" Any : narrow_mappings
        click Any href "../Any/"



      LLMIntrinsic : related_mappings





        LLMIntrinsic --> "*" Any : related_mappings
        click Any href "../Any/"



      LLMIntrinsic : requiredByTask





        LLMIntrinsic --> "*" AiTask : requiredByTask
        click AiTask href "../AiTask/"



      LLMIntrinsic : requiresCapability





        LLMIntrinsic --> "*" Capability : requiresCapability
        click Capability href "../Capability/"



      LLMIntrinsic : type

      LLMIntrinsic : url


```





## Inheritance
* [Entity](Entity.md)
    * [Entry](Entry.md)
        * **LLMIntrinsic**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [hasRelatedRisk](hasRelatedRisk.md) | * <br/> [Risk](Risk.md)&nbsp;or&nbsp;<br />[RiskConcept](RiskConcept.md)&nbsp;or&nbsp;<br />[Term](Term.md) | A relationship where an entity relates to a risk | direct |
| [hasRelatedTerm](hasRelatedTerm.md) | * <br/> [Term](Term.md)&nbsp;or&nbsp;<br />[RiskConcept](RiskConcept.md)&nbsp;or&nbsp;<br />[Term](Term.md) | A relationship where an entity relates to a term | direct |
| [hasDocumentation](hasDocumentation.md) | * <br/> [Documentation](Documentation.md) | Indicates documentation associated with an entity | direct |
| [isDefinedByVocabulary](isDefinedByVocabulary.md) | 0..1 <br/> [Vocabulary](Vocabulary.md) | A relationship where a term or a term group is defined by a vocabulary | direct |
| [hasAdapter](hasAdapter.md) | * <br/> [Adapter](Adapter.md) | The Adapter for the intrinsic | direct |
| [hasCapability](hasCapability.md) | * <br/> [Capability](Capability.md) | Indicates the technical capabilities this entry possesses | direct |
| [isDefinedByTaxonomy](isDefinedByTaxonomy.md) | 0..1 <br/> [Taxonomy](Taxonomy.md) | A relationship where a concept or a concept group is defined by a taxonomy | [Entry](Entry.md) |
| [isPartOf](isPartOf.md) | 0..1 <br/> [String](String.md) | A relationship where an entity is part of another entity | [Entry](Entry.md) |
| [requiredByTask](requiredByTask.md) | * <br/> [AiTask](AiTask.md) | Indicates that this entry is required to perform a specific AI task | [Entry](Entry.md) |
| [requiresCapability](requiresCapability.md) | * <br/> [Capability](Capability.md) | Indicates that this entry requires a specific capability | [Entry](Entry.md) |
| [implementedByAdapter](implementedByAdapter.md) | * <br/> [Adapter](Adapter.md) | Indicates that this capability is implemented by a specific adapter | [Entry](Entry.md) |
| [type](type.md) | 0..1 <br/> [String](String.md) |  | [Entry](Entry.md) |
| [id](id.md) | 1 <br/> [String](String.md) | A unique identifier to this instance of the model element | [Entity](Entity.md) |
| [name](name.md) | 0..1 <br/> [String](String.md) | A text name of this instance | [Entity](Entity.md) |
| [description](description.md) | 0..1 <br/> [String](String.md) | The description of an entity | [Entity](Entity.md) |
| [url](url.md) | 0..1 <br/> [Uri](Uri.md) | An optional URL associated with this instance | [Entity](Entity.md) |
| [dateCreated](dateCreated.md) | 0..1 <br/> [Date](Date.md) | The date on which the entity was created | [Entity](Entity.md) |
| [dateModified](dateModified.md) | 0..1 <br/> [Date](Date.md) | The date on which the entity was most recently modified | [Entity](Entity.md) |
| [exact_mappings](exact_mappings.md) | * <br/> [Any](Any.md) | The property is used to link two concepts, indicating a high degree of confid... | [Entity](Entity.md) |
| [close_mappings](close_mappings.md) | * <br/> [Any](Any.md) | The property is used to link two concepts that are sufficiently similar that ... | [Entity](Entity.md) |
| [related_mappings](related_mappings.md) | * <br/> [Any](Any.md) | The property skos:relatedMatch is used to state an associative mapping link b... | [Entity](Entity.md) |
| [narrow_mappings](narrow_mappings.md) | * <br/> [Any](Any.md) | The property is used to state a hierarchical mapping link between two concept... | [Entity](Entity.md) |
| [broad_mappings](broad_mappings.md) | * <br/> [Any](Any.md) | The property is used to state a hierarchical mapping link between two concept... | [Entity](Entity.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Container](Container.md) | [llmintrinsics](llmintrinsics.md) | range | [LLMIntrinsic](LLMIntrinsic.md) |
| [LLMIntrinsic](LLMIntrinsic.md) | [hasAdapter](hasAdapter.md) | domain | [LLMIntrinsic](LLMIntrinsic.md) |







## Identifier and Mapping Information






### Schema Source


* from schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:Capability |
| native | nexus:LLMIntrinsic |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: LLMIntrinsic
description: A capability that can be invoked through a well-defined API that is reasonably
  stable and independent of how the LLM intrinsic itself is implemented.
from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
is_a: Entry
slots:
- hasRelatedRisk
- hasRelatedTerm
- hasDocumentation
- isDefinedByVocabulary
- hasAdapter
- hasCapability
class_uri: ai:Capability

```
</details>

### Induced

<details>
```yaml
name: LLMIntrinsic
description: A capability that can be invoked through a well-defined API that is reasonably
  stable and independent of how the LLM intrinsic itself is implemented.
from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
is_a: Entry
attributes:
  hasRelatedRisk:
    name: hasRelatedRisk
    description: A relationship where an entity relates to a risk
    from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
    rank: 1000
    domain: Any
    alias: hasRelatedRisk
    owner: LLMIntrinsic
    domain_of:
    - Term
    - LLMQuestionPolicy
    - Action
    - AiEval
    - BenchmarkMetadataCard
    - Adapter
    - LLMIntrinsic
    range: Risk
    multivalued: true
    inlined: false
    any_of:
    - range: RiskConcept
    - range: Term
  hasRelatedTerm:
    name: hasRelatedTerm
    description: A relationship where an entity relates to a term
    from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
    rank: 1000
    domain: Any
    alias: hasRelatedTerm
    owner: LLMIntrinsic
    domain_of:
    - LLMIntrinsic
    range: Term
    multivalued: true
    inlined: false
    any_of:
    - range: RiskConcept
    - range: Term
  hasDocumentation:
    name: hasDocumentation
    description: Indicates documentation associated with an entity.
    from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
    rank: 1000
    slot_uri: airo:hasDocumentation
    alias: hasDocumentation
    owner: LLMIntrinsic
    domain_of:
    - Dataset
    - Vocabulary
    - Taxonomy
    - Concept
    - Group
    - Entry
    - Term
    - Principle
    - RiskTaxonomy
    - Action
    - BaseAi
    - LargeLanguageModelFamily
    - AiEval
    - BenchmarkMetadataCard
    - Adapter
    - LLMIntrinsic
    range: Documentation
    multivalued: true
    inlined: false
  isDefinedByVocabulary:
    name: isDefinedByVocabulary
    description: A relationship where a term or a term group is defined by a vocabulary
    from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
    rank: 1000
    slot_uri: schema:isPartOf
    alias: isDefinedByVocabulary
    owner: LLMIntrinsic
    domain_of:
    - Entry
    - Term
    - Adapter
    - LLMIntrinsic
    range: Vocabulary
  hasAdapter:
    name: hasAdapter
    description: The Adapter for the intrinsic
    from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
    rank: 1000
    domain: LLMIntrinsic
    alias: hasAdapter
    owner: LLMIntrinsic
    domain_of:
    - LLMIntrinsic
    range: Adapter
    multivalued: true
    inlined: false
  hasCapability:
    name: hasCapability
    description: 'Indicates the technical capabilities this entry possesses.

      '
    from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
    rank: 1000
    slot_uri: tech:hasCapability
    alias: hasCapability
    owner: LLMIntrinsic
    domain_of:
    - AiSystem
    - Adapter
    - LLMIntrinsic
    range: Capability
    multivalued: true
    inlined: false
  isDefinedByTaxonomy:
    name: isDefinedByTaxonomy
    description: A relationship where a concept or a concept group is defined by a
      taxonomy
    from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
    rank: 1000
    slot_uri: schema:isPartOf
    alias: isDefinedByTaxonomy
    owner: LLMIntrinsic
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
  isPartOf:
    name: isPartOf
    description: A relationship where an entity is part of another entity
    from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
    rank: 1000
    slot_uri: schema:isPartOf
    alias: isPartOf
    owner: LLMIntrinsic
    domain_of:
    - Entry
    - Risk
    - LargeLanguageModel
    - CapabilityGroup
    - Stakeholder
    range: string
  requiredByTask:
    name: requiredByTask
    description: Indicates that this entry is required to perform a specific AI task.
    from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
    rank: 1000
    alias: requiredByTask
    owner: LLMIntrinsic
    domain_of:
    - Entry
    - Capability
    inverse: requiresCapability
    range: AiTask
    multivalued: true
    inlined: false
  requiresCapability:
    name: requiresCapability
    description: Indicates that this entry requires a specific capability
    from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
    rank: 1000
    domain: Any
    alias: requiresCapability
    owner: LLMIntrinsic
    domain_of:
    - Entry
    - LargeLanguageModel
    - AiTask
    - Adapter
    inverse: requiredByTask
    range: Capability
    multivalued: true
    inlined: false
  implementedByAdapter:
    name: implementedByAdapter
    description: 'Indicates that this capability is implemented by a specific adapter.
      This relationship distinguishes the abstract capability (what can be done) from
      the technical implementation mechanism (how it is added/extended via adapters).

      '
    from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
    rank: 1000
    domain: Any
    alias: implementedByAdapter
    owner: LLMIntrinsic
    domain_of:
    - Entry
    - Capability
    inverse: implementsCapability
    range: Adapter
    multivalued: true
    inlined: false
  type:
    name: type
    from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/common
    designates_type: true
    alias: type
    owner: LLMIntrinsic
    domain_of:
    - Vocabulary
    - Taxonomy
    - Concept
    - Control
    - Group
    - Entry
    - Policy
    range: string
  id:
    name: id
    description: A unique identifier to this instance of the model element. Example
      identifiers include UUID, URI, URN, etc.
    from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
    rank: 1000
    slot_uri: schema:identifier
    identifier: true
    alias: id
    owner: LLMIntrinsic
    domain_of:
    - Entity
    range: string
    required: true
  name:
    name: name
    description: A text name of this instance.
    from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
    rank: 1000
    slot_uri: schema:name
    alias: name
    owner: LLMIntrinsic
    domain_of:
    - Entity
    - BenchmarkMetadataCard
    range: string
  description:
    name: description
    description: The description of an entity
    from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
    rank: 1000
    slot_uri: schema:description
    alias: description
    owner: LLMIntrinsic
    domain_of:
    - Entity
    range: string
  url:
    name: url
    description: An optional URL associated with this instance.
    from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
    rank: 1000
    slot_uri: schema:url
    alias: url
    owner: LLMIntrinsic
    domain_of:
    - Entity
    range: uri
  dateCreated:
    name: dateCreated
    description: The date on which the entity was created.
    from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
    rank: 1000
    slot_uri: schema:dateCreated
    alias: dateCreated
    owner: LLMIntrinsic
    domain_of:
    - Entity
    range: date
    required: false
  dateModified:
    name: dateModified
    description: The date on which the entity was most recently modified.
    from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
    rank: 1000
    slot_uri: schema:dateModified
    alias: dateModified
    owner: LLMIntrinsic
    domain_of:
    - Entity
    range: date
    required: false
  exact_mappings:
    name: exact_mappings
    description: The property is used to link two concepts, indicating a high degree
      of confidence that the concepts can be used interchangeably across a wide range
      of information retrieval applications
    from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
    rank: 1000
    slot_uri: skos:exactMatch
    alias: exact_mappings
    owner: LLMIntrinsic
    domain_of:
    - Entity
    range: Any
    multivalued: true
    inlined: false
  close_mappings:
    name: close_mappings
    description: The property is used to link two concepts that are sufficiently similar
      that they can be used interchangeably in some information retrieval applications.
    from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
    rank: 1000
    slot_uri: skos:closeMatch
    alias: close_mappings
    owner: LLMIntrinsic
    domain_of:
    - Entity
    range: Any
    multivalued: true
    inlined: false
  related_mappings:
    name: related_mappings
    description: The property skos:relatedMatch is used to state an associative mapping
      link between two concepts.
    from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
    rank: 1000
    slot_uri: skos:relatedMatch
    alias: related_mappings
    owner: LLMIntrinsic
    domain_of:
    - Entity
    range: Any
    multivalued: true
    inlined: false
  narrow_mappings:
    name: narrow_mappings
    description: The property is used to state a hierarchical mapping link between
      two concepts, indicating that the concept linked to, is a narrower concept than
      the originating concept.
    from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
    rank: 1000
    slot_uri: skos:narrowMatch
    alias: narrow_mappings
    owner: LLMIntrinsic
    domain_of:
    - Entity
    range: Any
    multivalued: true
    inlined: false
  broad_mappings:
    name: broad_mappings
    description: The property is used to state a hierarchical mapping link between
      two concepts, indicating that the concept linked to, is a broader concept than
      the originating concept.
    from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
    rank: 1000
    slot_uri: skos:broadMatch
    alias: broad_mappings
    owner: LLMIntrinsic
    domain_of:
    - Entity
    range: Any
    multivalued: true
    inlined: false
class_uri: ai:Capability

```
</details>
