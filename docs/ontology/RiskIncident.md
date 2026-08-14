---
search:
  boost: 10.0
---

# Class: RiskIncident

_An event occuring or occured which is a realised or materialised risk._

<div data-search-exclude markdown="1">

URI: [dpv-risk:Incident](https://w3id.org/dpv/risk#Incident)

```mermaid
 classDiagram
    class RiskIncident
    click RiskIncident href "../RiskIncident/"
      RiskConcept <|-- RiskIncident
        click RiskConcept href "../RiskConcept/"
      Entity <|-- RiskIncident
        click Entity href "../Entity/"

      RiskIncident : author

      RiskIncident : broad_mappings





        RiskIncident --> "*" Any : broad_mappings
        click Any href "../Any/"



      RiskIncident : close_mappings





        RiskIncident --> "*" Any : close_mappings
        click Any href "../Any/"



      RiskIncident : dateCreated

      RiskIncident : dateModified

      RiskIncident : description

      RiskIncident : exact_mappings





        RiskIncident --> "*" Any : exact_mappings
        click Any href "../Any/"



      RiskIncident : hasConsequence





        RiskIncident --> "0..1" Consequence : hasConsequence
        click Consequence href "../Consequence/"



      RiskIncident : hasDocumentation





        RiskIncident --> "*" Documentation : hasDocumentation
        click Documentation href "../Documentation/"



      RiskIncident : hasImpact





        RiskIncident --> "0..1" Impact : hasImpact
        click Impact href "../Impact/"



      RiskIncident : hasImpactOn





        RiskIncident --> "0..1" Impact : hasImpactOn
        click Impact href "../Impact/"



      RiskIncident : hasJurisdiction

      RiskIncident : hasLifecycleStatus





        RiskIncident --> "0..1" LifecycleStatus : hasLifecycleStatus
        click LifecycleStatus href "../LifecycleStatus/"



      RiskIncident : hasLikelihood





        RiskIncident --> "0..1" Likelihood : hasLikelihood
        click Likelihood href "../Likelihood/"



      RiskIncident : hasSeverity





        RiskIncident --> "0..1" Severity : hasSeverity
        click Severity href "../Severity/"



      RiskIncident : hasStatus





        RiskIncident --> "0..1" IncidentStatus : hasStatus
        click IncidentStatus href "../IncidentStatus/"



      RiskIncident : hasVariant





        RiskIncident --> "0..1" RiskIncident : hasVariant
        click RiskIncident href "../RiskIncident/"



      RiskIncident : id

      RiskIncident : isCategorizedAs





        RiskIncident --> "*" Any : isCategorizedAs
        click Any href "../Any/"



      RiskIncident : isDefinedByTaxonomy





        RiskIncident --> "0..1" Taxonomy : isDefinedByTaxonomy
        click Taxonomy href "../Taxonomy/"



      RiskIncident : isDetectedBy





        RiskIncident --> "*" RiskControl : isDetectedBy
        click RiskControl href "../RiskControl/"



      RiskIncident : isMitigatedBy





        RiskIncident --> "*" RiskControl : isMitigatedBy
        click RiskControl href "../RiskControl/"



      RiskIncident : isUsedWithinLocality





        RiskIncident --> "*" LocalityOfUse : isUsedWithinLocality
        click LocalityOfUse href "../LocalityOfUse/"



      RiskIncident : name

      RiskIncident : narrow_mappings





        RiskIncident --> "*" Any : narrow_mappings
        click Any href "../Any/"



      RiskIncident : notes

      RiskIncident : refersToRisk





        RiskIncident --> "*" Risk : refersToRisk
        click Risk href "../Risk/"



      RiskIncident : related_mappings





        RiskIncident --> "*" Any : related_mappings
        click Any href "../Any/"



      RiskIncident : source_uri

      RiskIncident : type

      RiskIncident : url


```

## Inheritance

- [Entity](Entity.md)
  - **RiskIncident** [ [RiskConcept](RiskConcept.md)]

## Class Properties

| Property  | Value                                                   |
| --------- | ------------------------------------------------------- |
| Class URI | [dpv-risk:Incident](https://w3id.org/dpv/risk#Incident) |

## Slots

| Name                                            | Cardinality and Range                                                                                                                                                                                                                 | Description                                                                      | Inheritance                   |
| ----------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | ----------------------------- |
| [refersToRisk](refersToRisk.md)                 | \* <br/> [Risk](Risk.md)                                                                                                                                                                                                              | Indicates the incident (subject) is a materialisation of the indicated risk (... | direct                        |
| [isDefinedByTaxonomy](isDefinedByTaxonomy.md)   | 0..1 <br/> [Taxonomy](Taxonomy.md)                                                                                                                                                                                                    | A relationship where a concept or a concept group is defined by a taxonomy       | direct                        |
| [hasStatus](hasStatus.md)                       | 0..1 <br/> [IncidentStatus](IncidentStatus.md)                                                                                                                                                                                        | Indicates the status of specified concept                                        | direct                        |
| [hasSeverity](hasSeverity.md)                   | 0..1 <br/> [Severity](Severity.md)                                                                                                                                                                                                    | Indicates the severity associated with a concept                                 | direct                        |
| [hasLikelihood](hasLikelihood.md)               | 0..1 <br/> [Likelihood](Likelihood.md)                                                                                                                                                                                                | The likelihood or probability or chance of something taking place or occuring    | direct                        |
| [hasImpactOn](hasImpactOn.md)                   | 0..1 <br/> [Impact](Impact.md)                                                                                                                                                                                                        | Indicates impact(s) possible or arising as consequences from specified concep... | direct                        |
| [hasConsequence](hasConsequence.md)             | 0..1 <br/> [Consequence](Consequence.md)                                                                                                                                                                                              | Indicates consequence(s) possible or arising from specified concept              | direct                        |
| [hasImpact](hasImpact.md)                       | 0..1 <br/> [Impact](Impact.md)                                                                                                                                                                                                        | Indicates impact(s) possible or arising as consequences from specified concep... | direct                        |
| [hasVariant](hasVariant.md)                     | 0..1 <br/> [RiskIncident](RiskIncident.md)                                                                                                                                                                                            | Indicates an incident that shares the same causative factors, produces simila... | direct                        |
| [author](author.md)                             | 0..1 <br/> [String](String.md)                                                                                                                                                                                                        | The author or authors of the incident report                                     | direct                        |
| [source_uri](source_uri.md)                     | 0..1 <br/> [String](String.md)                                                                                                                                                                                                        | The uri of the incident                                                          | direct                        |
| [isDetectedBy](isDetectedBy.md)                 | \* <br/> [RiskControl](RiskControl.md)                                                                                                                                                                                                | A relationship where a risk, risk source, consequence, or impact is detected ... | [RiskConcept](RiskConcept.md) |
| [isMitigatedBy](isMitigatedBy.md)               | \* <br/> [RiskControl](RiskControl.md)                                                                                                                                                                                                | A relationship where a risk, risk source, consequence, or impact is mitigated... | [RiskConcept](RiskConcept.md) |
| [isUsedWithinLocality](isUsedWithinLocality.md) | \* <br/> [LocalityOfUse](LocalityOfUse.md)                                                                                                                                                                                            | Specifies the domain an AI system is used within                                 | [RiskConcept](RiskConcept.md) |
| [id](id.md)                                     | 1 <br/> [String](String.md)                                                                                                                                                                                                           | A unique identifier to this instance of the model element                        | [Entity](Entity.md)           |
| [name](name.md)                                 | 0..1 <br/> [String](String.md)                                                                                                                                                                                                        | A text name of this instance                                                     | [Entity](Entity.md)           |
| [description](description.md)                   | 0..1 <br/> [String](String.md)                                                                                                                                                                                                        | The description of an entity                                                     | [Entity](Entity.md)           |
| [url](url.md)                                   | 0..1 <br/> [Uri](Uri.md)                                                                                                                                                                                                              | An optional URL associated with this instance                                    | [Entity](Entity.md)           |
| [dateCreated](dateCreated.md)                   | 0..1 <br/> [Date](Date.md)                                                                                                                                                                                                            | The date on which the entity was created                                         | [Entity](Entity.md)           |
| [dateModified](dateModified.md)                 | 0..1 <br/> [Date](Date.md)                                                                                                                                                                                                            | The date on which the entity was most recently modified                          | [Entity](Entity.md)           |
| [exact_mappings](exact_mappings.md)             | \* <br/> [Any](Any.md)                                                                                                                                                                                                                | The property is used to link two concepts, indicating a high degree of confid... | [Entity](Entity.md)           |
| [close_mappings](close_mappings.md)             | \* <br/> [Any](Any.md)                                                                                                                                                                                                                | The property is used to link two concepts that are sufficiently similar that ... | [Entity](Entity.md)           |
| [related_mappings](related_mappings.md)         | \* <br/> [Any](Any.md)                                                                                                                                                                                                                | The property skos:relatedMatch is used to state an associative mapping link b... | [Entity](Entity.md)           |
| [narrow_mappings](narrow_mappings.md)           | \* <br/> [Any](Any.md)                                                                                                                                                                                                                | The property is used to state a hierarchical mapping link between two concept... | [Entity](Entity.md)           |
| [broad_mappings](broad_mappings.md)             | \* <br/> [Any](Any.md)                                                                                                                                                                                                                | The property is used to state a hierarchical mapping link between two concept... | [Entity](Entity.md)           |
| [isCategorizedAs](isCategorizedAs.md)           | \* <br/> [Any](Any.md)                                                                                                                                                                                                                | A relationship where an entity has been deemed to be categorized                 | [Entity](Entity.md)           |
| [hasLifecycleStatus](hasLifecycleStatus.md)     | 0..1 <br/> [LifecycleStatus](LifecycleStatus.md)                                                                                                                                                                                      | The editorial / publication lifecycle state of this entity                       | [Entity](Entity.md)           |
| [notes](notes.md)                               | \* <br/> [String](String.md)                                                                                                                                                                                                          | Free-text editorial notes, source breadcrumbs, or build-time provenance that ... | [Entity](Entity.md)           |
| [hasDocumentation](hasDocumentation.md)         | \* <br/> [Documentation](Documentation.md)                                                                                                                                                                                            | Indicates documentation associated with an entity                                | [Concept](Concept.md)         |
| [hasJurisdiction](hasJurisdiction.md)           | \* <br/> [String](String.md)&nbsp;or&nbsp;<br />[Jurisdiction](Jurisdiction.md)&nbsp;or&nbsp;<br />[SupraNationalJurisdiction](SupraNationalJurisdiction.md)&nbsp;or&nbsp;<br />[SubnationalJurisdiction](SubnationalJurisdiction.md) | The legal or regulatory jurisdiction(s) applicable to an AI system, policy, r... | [Concept](Concept.md)         |
| [type](type.md)                                 | 0..1 <br/> [String](String.md)                                                                                                                                                                                                        | The type or class designation of this entity instance                            | [Concept](Concept.md)         |

## Usages

| used by                         | used in                           | type   | used                            |
| ------------------------------- | --------------------------------- | ------ | ------------------------------- |
| [Container](Container.md)       | [riskincidents](riskincidents.md) | range  | [RiskIncident](RiskIncident.md) |
| [RiskIncident](RiskIncident.md) | [refersToRisk](refersToRisk.md)   | domain | [RiskIncident](RiskIncident.md) |
| [RiskIncident](RiskIncident.md) | [hasVariant](hasVariant.md)       | domain | [RiskIncident](RiskIncident.md) |
| [RiskIncident](RiskIncident.md) | [hasVariant](hasVariant.md)       | range  | [RiskIncident](RiskIncident.md) |

## Identifier and Mapping Information

### Schema Source

- from schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology

## Mappings

| Mapping Type | Mapped Value       |
| ------------ | ------------------ |
| self         | dpv-risk:Incident  |
| native       | nexus:RiskIncident |

## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: RiskIncident
description: An event occuring or occured which is a realised or materialised risk.
from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
is_a: Entity
mixins:
- RiskConcept
slots:
- refersToRisk
- isDefinedByTaxonomy
- hasStatus
- hasSeverity
- hasLikelihood
- hasImpactOn
- hasConsequence
- hasImpact
- hasVariant
attributes:
  author:
    name: author
    description: The author or authors of the incident report
    from_schema: https://w3id.org/ai-atlas-nexus/ai_risk
    domain_of:
    - Documentation
    - RiskIncident
  source_uri:
    name: source_uri
    description: The uri of the incident
    from_schema: https://w3id.org/ai-atlas-nexus/ai_risk
    rank: 1000
    domain_of:
    - RiskIncident
class_uri: dpv-risk:Incident

````
</details>

### Induced

<details>
```yaml
name: RiskIncident
description: An event occuring or occured which is a realised or materialised risk.
from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
is_a: Entity
mixins:
- RiskConcept
attributes:
  author:
    name: author
    description: The author or authors of the incident report
    from_schema: https://w3id.org/ai-atlas-nexus/ai_risk
    owner: RiskIncident
    domain_of:
    - Documentation
    - RiskIncident
    range: string
  source_uri:
    name: source_uri
    description: The uri of the incident
    from_schema: https://w3id.org/ai-atlas-nexus/ai_risk
    rank: 1000
    owner: RiskIncident
    domain_of:
    - RiskIncident
    range: string
  refersToRisk:
    name: refersToRisk
    description: Indicates the incident (subject) is a materialisation of the indicated
      risk (object)
    from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
    exact_mappings:
    - dpv:refersToRisk
    rank: 1000
    domain: RiskIncident
    owner: RiskIncident
    domain_of:
    - RiskIncident
    range: Risk
    multivalued: true
    inlined: false
  isDefinedByTaxonomy:
    name: isDefinedByTaxonomy
    description: A relationship where a concept or a concept group is defined by a
      taxonomy
    from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
    rank: 1000
    slot_uri: schema:isPartOf
    owner: RiskIncident
    domain_of:
    - Concept
    - Control
    - Group
    - Entry
    - Policy
    - Rule
    - RiskControlGroup
    - RiskGroup
    - Risk
    - RiskControl
    - Action
    - RiskIncident
    - CapabilityGroup
    - AiTaskDomain
    - AiTaskGroup
    - Stakeholder
    - StakeholderGroup
    - Requirement
    range: Taxonomy
  hasStatus:
    name: hasStatus
    description: Indicates the status of specified concept
    from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
    rank: 1000
    domain: RiskConcept
    owner: RiskIncident
    domain_of:
    - RiskIncident
    range: IncidentStatus
  hasSeverity:
    name: hasSeverity
    description: Indicates the severity associated with a concept
    from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
    rank: 1000
    domain: RiskConcept
    owner: RiskIncident
    domain_of:
    - RiskIncident
    range: Severity
  hasLikelihood:
    name: hasLikelihood
    description: The likelihood or probability or chance of something taking place
      or occuring
    from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
    rank: 1000
    domain: RiskConcept
    owner: RiskIncident
    domain_of:
    - RiskIncident
    range: Likelihood
  hasImpactOn:
    name: hasImpactOn
    description: Indicates impact(s) possible or arising as consequences from specified
      concept
    from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
    broad_mappings:
    - dpv:hasConsequenceOn
    rank: 1000
    domain: RiskConcept
    owner: RiskIncident
    domain_of:
    - RiskIncident
    range: Impact
  hasConsequence:
    name: hasConsequence
    description: Indicates consequence(s) possible or arising from specified concept
    from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
    rank: 1000
    domain: RiskConcept
    owner: RiskIncident
    domain_of:
    - RiskIncident
    range: Consequence
  hasImpact:
    name: hasImpact
    description: Indicates impact(s) possible or arising as consequences from specified
      concept
    from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
    broad_mappings:
    - dpv:hasConsequence
    rank: 1000
    domain: RiskConcept
    owner: RiskIncident
    domain_of:
    - RiskIncident
    range: Impact
  hasVariant:
    name: hasVariant
    description: Indicates an incident that shares the same causative factors, produces
      similar harms, and involves the same intelligent systems as a known AI incident.
    from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
    rank: 1000
    domain: RiskIncident
    owner: RiskIncident
    domain_of:
    - RiskIncident
    range: RiskIncident
  isDetectedBy:
    name: isDetectedBy
    description: A relationship where a risk, risk source, consequence, or impact
      is detected by a risk control.
    from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
    rank: 1000
    domain: RiskConcept
    owner: RiskIncident
    domain_of:
    - RiskConcept
    inverse: detectsRiskConcept
    range: RiskControl
    multivalued: true
    inlined: false
  isMitigatedBy:
    name: isMitigatedBy
    description: A relationship where a risk, risk source, consequence, or impact
      is mitigated by a risk control.
    from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
    rank: 1000
    domain: RiskConcept
    owner: RiskIncident
    domain_of:
    - RiskConcept
    inverse: mitigatesRiskConcept
    range: RiskControl
    multivalued: true
    inlined: false
  isUsedWithinLocality:
    name: isUsedWithinLocality
    description: Specifies the domain an AI system is used within.
    from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
    rank: 1000
    slot_uri: airo:isUsedWithinLocality
    owner: RiskIncident
    domain_of:
    - RiskConcept
    - AiSystem
    range: LocalityOfUse
    multivalued: true
    inlined: false
  id:
    name: id
    description: A unique identifier to this instance of the model element. Example
      identifiers include UUID, URI, URN, etc.
    from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
    rank: 1000
    slot_uri: schema:identifier
    identifier: true
    owner: RiskIncident
    domain_of:
    - Entity
    range: string
    required: true
  name:
    name: name
    description: A text name of this instance.
    from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
    rank: 1000
    slot_uri: schema:name
    owner: RiskIncident
    domain_of:
    - Entity
    - BenchmarkMetadataCard
    range: string
  description:
    name: description
    description: The description of an entity
    from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
    rank: 1000
    slot_uri: schema:description
    owner: RiskIncident
    domain_of:
    - Entity
    range: string
  url:
    name: url
    description: An optional URL associated with this instance.
    from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
    rank: 1000
    slot_uri: schema:url
    owner: RiskIncident
    domain_of:
    - Entity
    range: uri
  dateCreated:
    name: dateCreated
    description: The date on which the entity was created.
    from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
    rank: 1000
    slot_uri: schema:dateCreated
    owner: RiskIncident
    domain_of:
    - Entity
    range: date
    required: false
  dateModified:
    name: dateModified
    description: The date on which the entity was most recently modified.
    from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
    rank: 1000
    slot_uri: schema:dateModified
    owner: RiskIncident
    domain_of:
    - Entity
    range: date
    required: false
  exact_mappings:
    name: exact_mappings
    description: The property is used to link two concepts, indicating a high degree
      of confidence that the concepts can be used interchangeably across a wide range
      of information retrieval applications
    from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
    rank: 1000
    slot_uri: skos:exactMatch
    owner: RiskIncident
    domain_of:
    - Entity
    range: Any
    multivalued: true
    inlined: false
  close_mappings:
    name: close_mappings
    description: The property is used to link two concepts that are sufficiently similar
      that they can be used interchangeably in some information retrieval applications.
    from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
    rank: 1000
    slot_uri: skos:closeMatch
    owner: RiskIncident
    domain_of:
    - Entity
    range: Any
    multivalued: true
    inlined: false
  related_mappings:
    name: related_mappings
    description: The property skos:relatedMatch is used to state an associative mapping
      link between two concepts.
    from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
    rank: 1000
    slot_uri: skos:relatedMatch
    owner: RiskIncident
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
    from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
    rank: 1000
    slot_uri: skos:narrowMatch
    owner: RiskIncident
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
    from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
    rank: 1000
    slot_uri: skos:broadMatch
    owner: RiskIncident
    domain_of:
    - Entity
    range: Any
    multivalued: true
    inlined: false
  isCategorizedAs:
    name: isCategorizedAs
    description: A relationship where an entity has been deemed to be categorized
    from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
    rank: 1000
    slot_uri: nexus:isCategorizedAs
    owner: RiskIncident
    domain_of:
    - Entity
    range: Any
    multivalued: true
    inlined: false
  hasLifecycleStatus:
    name: hasLifecycleStatus
    description: The editorial / publication lifecycle state of this entity. Distinct
      from AiLifecyclePhase, which describes an AI system's runtime evolution rather
      than the editorial workflow of a catalogued entry.
    from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
    aliases:
    - lifecycle_status
    - doc_status
    rank: 1000
    slot_uri: adms:status
    owner: RiskIncident
    domain_of:
    - Entity
    range: LifecycleStatus
  notes:
    name: notes
    description: Free-text editorial notes, source breadcrumbs, or build-time provenance
      that do not belong in the user-facing description. Opaque to consumers.
    from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
    rank: 1000
    slot_uri: skos:note
    owner: RiskIncident
    domain_of:
    - Entity
    range: string
    recommended: false
    multivalued: true
  hasDocumentation:
    name: hasDocumentation
    description: Indicates documentation associated with an entity.
    from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
    rank: 1000
    slot_uri: airo:hasDocumentation
    owner: RiskIncident
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
    - RiskControlGroupTaxonomy
    - Action
    - BaseAi
    - LargeLanguageModelFamily
    - AiTaskTaxonomy
    - AiEval
    - EveryEvalAIResult
    - BenchmarkMetadataCard
    - Adapter
    - LLMIntrinsic
    range: Documentation
    multivalued: true
    inlined: false
  hasJurisdiction:
    name: hasJurisdiction
    description: The legal or regulatory jurisdiction(s) applicable to an AI system,
      policy, risk, or obligation. Accepts ISO 3166-1 country codes, supra-national
      bodies, or subnational jurisdictions with distinct regulatory significance.
      Aligns with dpv:hasJurisdiction.
    from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
    see_also:
    - https://w3id.org/dpv#hasJurisdiction
    rank: 1000
    slot_uri: dpv:hasJurisdiction
    owner: RiskIncident
    domain_of:
    - Concept
    range: string
    multivalued: true
    inlined: false
    any_of:
    - range: Jurisdiction
    - range: SupraNationalJurisdiction
    - range: SubnationalJurisdiction
  type:
    name: type
    description: The type or class designation of this entity instance.
    from_schema: https://w3id.org/ai-atlas-nexus/common
    designates_type: true
    owner: RiskIncident
    domain_of:
    - Vocabulary
    - Taxonomy
    - Concept
    - Control
    - Group
    - Entry
    - Policy
    - Rule
    - Permission
    - Prohibition
    - Obligation
    - Recommendation
    - Certification
    - BenchmarkMetadataCard
    - ControlActivity
    - ControlActivityPermission
    - ControlActivityProhibition
    - ControlActivityObligation
    - ControlActivityRecommendation
    - Requirement
    range: string
class_uri: dpv-risk:Incident

````

</details></div>
