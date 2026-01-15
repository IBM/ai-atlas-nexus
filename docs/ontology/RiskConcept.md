

# Class: RiskConcept


_An umbrella term for referring to risk, risk source, consequence and impact._





URI: [airo:RiskConcept](https://w3id.org/airo#RiskConcept)





```mermaid
 classDiagram
    class RiskConcept
    click RiskConcept href "../RiskConcept/"
      Concept <|-- RiskConcept
        click Concept href "../Concept/"


      RiskConcept <|-- RiskGroup
        click RiskGroup href "../RiskGroup/"
      RiskConcept <|-- Risk
        click Risk href "../Risk/"
      RiskConcept <|-- RiskControl
        click RiskControl href "../RiskControl/"
      RiskConcept <|-- RiskIncident
        click RiskIncident href "../RiskIncident/"
      RiskConcept <|-- Impact
        click Impact href "../Impact/"


      RiskConcept : broad_mappings





        RiskConcept --> "*" Any : broad_mappings
        click Any href "../Any/"



      RiskConcept : close_mappings





        RiskConcept --> "*" Any : close_mappings
        click Any href "../Any/"



      RiskConcept : dateCreated

      RiskConcept : dateModified

      RiskConcept : description

      RiskConcept : exact_mappings





        RiskConcept --> "*" Any : exact_mappings
        click Any href "../Any/"



      RiskConcept : hasDocumentation





        RiskConcept --> "*" Documentation : hasDocumentation
        click Documentation href "../Documentation/"



      RiskConcept : id

      RiskConcept : isDefinedByTaxonomy





        RiskConcept --> "0..1" Taxonomy : isDefinedByTaxonomy
        click Taxonomy href "../Taxonomy/"



      RiskConcept : isDetectedBy





        RiskConcept --> "*" RiskControl : isDetectedBy
        click RiskControl href "../RiskControl/"



      RiskConcept : name

      RiskConcept : narrow_mappings





        RiskConcept --> "*" Any : narrow_mappings
        click Any href "../Any/"



      RiskConcept : related_mappings





        RiskConcept --> "*" Any : related_mappings
        click Any href "../Any/"



      RiskConcept : type

      RiskConcept : url


```





## Inheritance
* [Entity](Entity.md)
    * [Concept](Concept.md)
        * **RiskConcept**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [isDetectedBy](isDetectedBy.md) | * <br/> [RiskControl](RiskControl.md) | A relationship where a risk, risk source, consequence, or impact is detected ... | direct |
| [isDefinedByTaxonomy](isDefinedByTaxonomy.md) | 0..1 <br/> [Taxonomy](Taxonomy.md) | A relationship where a concept or a concept group is defined by a taxonomy | [Concept](Concept.md) |
| [hasDocumentation](hasDocumentation.md) | * <br/> [Documentation](Documentation.md) | Indicates documentation associated with an entity | [Concept](Concept.md) |
| [type](type.md) | 0..1 <br/> [String](String.md) |  | [Concept](Concept.md) |
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



## Mixin Usage

| mixed into | description |
| --- | --- |
| [RiskGroup](RiskGroup.md) | A group of AI system related risks that are part of a risk taxonomy |
| [Risk](Risk.md) | The state of uncertainty associated with an AI system, that has the potential... |
| [RiskControl](RiskControl.md) | A measure that maintains and/or modifies risk (and risk concepts) |
| [RiskIncident](RiskIncident.md) | An event occuring or occured which is a realised or materialised risk |
| [Impact](Impact.md) |  |




## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Term](Term.md) | [hasRelatedRisk](hasRelatedRisk.md) | any_of[range] | [RiskConcept](RiskConcept.md) |
| [LLMQuestionPolicy](LLMQuestionPolicy.md) | [hasRelatedRisk](hasRelatedRisk.md) | any_of[range] | [RiskConcept](RiskConcept.md) |
| [RiskGroup](RiskGroup.md) | [isDetectedBy](isDetectedBy.md) | domain | [RiskConcept](RiskConcept.md) |
| [Risk](Risk.md) | [detectsRiskConcept](detectsRiskConcept.md) | range | [RiskConcept](RiskConcept.md) |
| [Risk](Risk.md) | [isDetectedBy](isDetectedBy.md) | domain | [RiskConcept](RiskConcept.md) |
| [RiskConcept](RiskConcept.md) | [isDetectedBy](isDetectedBy.md) | domain | [RiskConcept](RiskConcept.md) |
| [RiskControl](RiskControl.md) | [detectsRiskConcept](detectsRiskConcept.md) | range | [RiskConcept](RiskConcept.md) |
| [RiskControl](RiskControl.md) | [isDetectedBy](isDetectedBy.md) | domain | [RiskConcept](RiskConcept.md) |
| [Action](Action.md) | [hasRelatedRisk](hasRelatedRisk.md) | any_of[range] | [RiskConcept](RiskConcept.md) |
| [Action](Action.md) | [detectsRiskConcept](detectsRiskConcept.md) | range | [RiskConcept](RiskConcept.md) |
| [Action](Action.md) | [isDetectedBy](isDetectedBy.md) | domain | [RiskConcept](RiskConcept.md) |
| [RiskIncident](RiskIncident.md) | [hasStatus](hasStatus.md) | domain | [RiskConcept](RiskConcept.md) |
| [RiskIncident](RiskIncident.md) | [hasSeverity](hasSeverity.md) | domain | [RiskConcept](RiskConcept.md) |
| [RiskIncident](RiskIncident.md) | [hasLikelihood](hasLikelihood.md) | domain | [RiskConcept](RiskConcept.md) |
| [RiskIncident](RiskIncident.md) | [hasImpactOn](hasImpactOn.md) | domain | [RiskConcept](RiskConcept.md) |
| [RiskIncident](RiskIncident.md) | [hasConsequence](hasConsequence.md) | domain | [RiskConcept](RiskConcept.md) |
| [RiskIncident](RiskIncident.md) | [hasImpact](hasImpact.md) | domain | [RiskConcept](RiskConcept.md) |
| [RiskIncident](RiskIncident.md) | [isDetectedBy](isDetectedBy.md) | domain | [RiskConcept](RiskConcept.md) |
| [Impact](Impact.md) | [isDetectedBy](isDetectedBy.md) | domain | [RiskConcept](RiskConcept.md) |
| [AiEval](AiEval.md) | [hasRelatedRisk](hasRelatedRisk.md) | any_of[range] | [RiskConcept](RiskConcept.md) |
| [BenchmarkMetadataCard](BenchmarkMetadataCard.md) | [hasRelatedRisk](hasRelatedRisk.md) | any_of[range] | [RiskConcept](RiskConcept.md) |
| [Question](Question.md) | [hasRelatedRisk](hasRelatedRisk.md) | any_of[range] | [RiskConcept](RiskConcept.md) |
| [Questionnaire](Questionnaire.md) | [hasRelatedRisk](hasRelatedRisk.md) | any_of[range] | [RiskConcept](RiskConcept.md) |
| [Adapter](Adapter.md) | [hasRelatedRisk](hasRelatedRisk.md) | any_of[range] | [RiskConcept](RiskConcept.md) |
| [LLMIntrinsic](LLMIntrinsic.md) | [hasRelatedRisk](hasRelatedRisk.md) | any_of[range] | [RiskConcept](RiskConcept.md) |
| [LLMIntrinsic](LLMIntrinsic.md) | [hasRelatedTerm](hasRelatedTerm.md) | any_of[range] | [RiskConcept](RiskConcept.md) |







## Identifier and Mapping Information






### Schema Source


* from schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | airo:RiskConcept |
| native | nexus:RiskConcept |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: RiskConcept
description: An umbrella term for referring to risk, risk source, consequence and
  impact.
from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
is_a: Concept
mixin: true
slots:
- isDetectedBy
class_uri: airo:RiskConcept

```
</details>

### Induced

<details>
```yaml
name: RiskConcept
description: An umbrella term for referring to risk, risk source, consequence and
  impact.
from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
is_a: Concept
mixin: true
attributes:
  isDetectedBy:
    name: isDetectedBy
    description: A relationship where a risk, risk source, consequence, or impact
      is detected by a risk control.
    from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
    rank: 1000
    domain: RiskConcept
    alias: isDetectedBy
    owner: RiskConcept
    domain_of:
    - RiskConcept
    inverse: detectsRiskConcept
    range: RiskControl
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
    owner: RiskConcept
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
  hasDocumentation:
    name: hasDocumentation
    description: Indicates documentation associated with an entity.
    from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
    rank: 1000
    slot_uri: airo:hasDocumentation
    alias: hasDocumentation
    owner: RiskConcept
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
  type:
    name: type
    from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/common
    designates_type: true
    alias: type
    owner: RiskConcept
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
    owner: RiskConcept
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
    owner: RiskConcept
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
    owner: RiskConcept
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
    owner: RiskConcept
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
    owner: RiskConcept
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
    owner: RiskConcept
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
    owner: RiskConcept
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
    owner: RiskConcept
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
    owner: RiskConcept
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
    owner: RiskConcept
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
    owner: RiskConcept
    domain_of:
    - Entity
    range: Any
    multivalued: true
    inlined: false
class_uri: airo:RiskConcept

```
</details>
