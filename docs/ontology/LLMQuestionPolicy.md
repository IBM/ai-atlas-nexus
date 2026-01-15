

# Class: LLMQuestionPolicy


_The policy guides how the language model should answer a diverse set of sensitive questions._





URI: [nexus:LLMQuestionPolicy](https://ibm.github.io/ai-atlas-nexus/ontology/LLMQuestionPolicy)





```mermaid
 classDiagram
    class LLMQuestionPolicy
    click LLMQuestionPolicy href "../LLMQuestionPolicy/"
      Policy <|-- LLMQuestionPolicy
        click Policy href "../Policy/"

      LLMQuestionPolicy : broad_mappings





        LLMQuestionPolicy --> "*" Any : broad_mappings
        click Any href "../Any/"



      LLMQuestionPolicy : close_mappings





        LLMQuestionPolicy --> "*" Any : close_mappings
        click Any href "../Any/"



      LLMQuestionPolicy : dateCreated

      LLMQuestionPolicy : dateModified

      LLMQuestionPolicy : description

      LLMQuestionPolicy : exact_mappings





        LLMQuestionPolicy --> "*" Any : exact_mappings
        click Any href "../Any/"



      LLMQuestionPolicy : hasException

      LLMQuestionPolicy : hasReasonDenial

      LLMQuestionPolicy : hasRelatedRisk





        LLMQuestionPolicy --> "*" Risk : hasRelatedRisk
        click Risk href "../Risk/"



      LLMQuestionPolicy : hasRule





        LLMQuestionPolicy --> "*" Rule : hasRule
        click Rule href "../Rule/"



      LLMQuestionPolicy : hasShortReplyType

      LLMQuestionPolicy : id

      LLMQuestionPolicy : isDefinedByTaxonomy





        LLMQuestionPolicy --> "0..1" Taxonomy : isDefinedByTaxonomy
        click Taxonomy href "../Taxonomy/"



      LLMQuestionPolicy : name

      LLMQuestionPolicy : narrow_mappings





        LLMQuestionPolicy --> "*" Any : narrow_mappings
        click Any href "../Any/"



      LLMQuestionPolicy : related_mappings





        LLMQuestionPolicy --> "*" Any : related_mappings
        click Any href "../Any/"



      LLMQuestionPolicy : type

      LLMQuestionPolicy : url


```





## Inheritance
* [Entity](Entity.md)
    * [Policy](Policy.md)
        * **LLMQuestionPolicy**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [hasRelatedRisk](hasRelatedRisk.md) | * <br/> [Risk](Risk.md)&nbsp;or&nbsp;<br />[RiskConcept](RiskConcept.md)&nbsp;or&nbsp;<br />[Term](Term.md) | A relationship where an entity relates to a risk | direct |
| [hasRule](hasRule.md) | * <br/> [Rule](Rule.md) | Specifying applicability or inclusion of a rule within specified context | direct |
| [hasReasonDenial](hasReasonDenial.md) | 0..1 <br/> [String](String.md) | Reason for denial | direct |
| [hasShortReplyType](hasShortReplyType.md) | 0..1 <br/> [String](String.md) | Short reply type | direct |
| [hasException](hasException.md) | 0..1 <br/> [String](String.md) | Exception type | direct |
| [isDefinedByTaxonomy](isDefinedByTaxonomy.md) | 0..1 <br/> [Taxonomy](Taxonomy.md) | A relationship where a concept or a concept group is defined by a taxonomy | [Policy](Policy.md) |
| [type](type.md) | 0..1 <br/> [String](String.md) |  | [Policy](Policy.md) |
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










## Identifier and Mapping Information






### Schema Source


* from schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | nexus:LLMQuestionPolicy |
| native | nexus:LLMQuestionPolicy |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: LLMQuestionPolicy
description: The policy guides how the language model should answer a diverse set
  of sensitive questions.
from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
is_a: Policy
slots:
- hasRelatedRisk
- hasRule
- hasReasonDenial
- hasShortReplyType
- hasException

```
</details>

### Induced

<details>
```yaml
name: LLMQuestionPolicy
description: The policy guides how the language model should answer a diverse set
  of sensitive questions.
from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
is_a: Policy
attributes:
  hasRelatedRisk:
    name: hasRelatedRisk
    description: A relationship where an entity relates to a risk
    from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
    rank: 1000
    domain: Any
    alias: hasRelatedRisk
    owner: LLMQuestionPolicy
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
  hasRule:
    name: hasRule
    description: Specifying applicability or inclusion of a rule within specified
      context.
    from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
    rank: 1000
    slot_uri: dpv:hasRule
    alias: hasRule
    owner: LLMQuestionPolicy
    domain_of:
    - LLMQuestionPolicy
    range: Rule
    multivalued: true
    inlined: false
  hasReasonDenial:
    name: hasReasonDenial
    description: Reason for denial
    from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
    rank: 1000
    slot_uri: nexus:hasReasonDenial
    alias: hasReasonDenial
    owner: LLMQuestionPolicy
    domain_of:
    - LLMQuestionPolicy
    range: string
    multivalued: false
    inlined: true
  hasShortReplyType:
    name: hasShortReplyType
    description: Short reply type
    from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
    rank: 1000
    slot_uri: nexus:hasShortReplyType
    alias: hasShortReplyType
    owner: LLMQuestionPolicy
    domain_of:
    - LLMQuestionPolicy
    range: string
    multivalued: false
    inlined: true
  hasException:
    name: hasException
    description: Exception type
    from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
    rank: 1000
    slot_uri: nexus:hasException
    alias: hasException
    owner: LLMQuestionPolicy
    domain_of:
    - LLMQuestionPolicy
    range: string
    multivalued: false
    inlined: true
  isDefinedByTaxonomy:
    name: isDefinedByTaxonomy
    description: A relationship where a concept or a concept group is defined by a
      taxonomy
    from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
    rank: 1000
    slot_uri: schema:isPartOf
    alias: isDefinedByTaxonomy
    owner: LLMQuestionPolicy
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
  type:
    name: type
    from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/common
    designates_type: true
    alias: type
    owner: LLMQuestionPolicy
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
    owner: LLMQuestionPolicy
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
    owner: LLMQuestionPolicy
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
    owner: LLMQuestionPolicy
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
    owner: LLMQuestionPolicy
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
    owner: LLMQuestionPolicy
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
    owner: LLMQuestionPolicy
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
    owner: LLMQuestionPolicy
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
    owner: LLMQuestionPolicy
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
    owner: LLMQuestionPolicy
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
    owner: LLMQuestionPolicy
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
    owner: LLMQuestionPolicy
    domain_of:
    - Entity
    range: Any
    multivalued: true
    inlined: false

```
</details>
