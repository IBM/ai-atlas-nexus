---
search:
  boost: 2.0
---

# Enum: LifecycleStatus

_Editorial / publication state of a catalogued entity. Permissible values align to the ADMS-status codelist where one exists; otherwise drawn from PSO vocabulary, and failing that, minted in this nexus namespace._

<div data-search-exclude markdown="1">

URI: [nexus:LifecycleStatus](https://w3id.org/ai-atlas-nexus/LifecycleStatus)

## Permissible Values

| Value      | Meaning                      | Description                                 |
| ---------- | ---------------------------- | ------------------------------------------- |
| DRAFT      | adms-status:UnderDevelopment | Initial draft under development             |
| REVIEW     | pso:under-review             | Under editorial or technical review         |
| APPROVED   | adms-status:Completed        | Approved / published as authoritative       |
| DEPRECATED | adms-status:Deprecated       | Discouraged for new use but still available |
| SUPERSEDED | None                         | Replaced by a newer version of this entity  |
| WITHDRAWN  | adms-status:Withdrawn        | Removed / no longer available               |

## Slots

| Name                                        | Description                                                |
| ------------------------------------------- | ---------------------------------------------------------- |
| [hasLifecycleStatus](hasLifecycleStatus.md) | The editorial / publication lifecycle state of this entity |

## See Also

- [https://semiceu.github.io/ADMS/releases/2.00/](https://semiceu.github.io/ADMS/releases/2.00/)
- [http://purl.org/adms/status/1.0](http://purl.org/adms/status/1.0)
- [https://sparontologies.github.io/pso/current/pso.html](https://sparontologies.github.io/pso/current/pso.html)

## Identifier and Mapping Information

### Schema Source

- from schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology

## LinkML Source

<details>
```yaml
name: LifecycleStatus
description: Editorial / publication state of a catalogued entity. Permissible values
  align to the ADMS-status codelist where one exists; otherwise drawn from PSO vocabulary,
  and failing that, minted in this nexus namespace.
from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
see_also:
- https://semiceu.github.io/ADMS/releases/2.00/
- http://purl.org/adms/status/1.0
- https://sparontologies.github.io/pso/current/pso.html
rank: 1000
permissible_values:
  DRAFT:
    text: DRAFT
    description: Initial draft under development.
    meaning: adms-status:UnderDevelopment
  REVIEW:
    text: REVIEW
    description: Under editorial or technical review.
    meaning: pso:under-review
    comments:
    - No ADMS equivalent. PSO covers peer review which is sufficient.
  APPROVED:
    text: APPROVED
    description: Approved / published as authoritative.
    meaning: adms-status:Completed
  DEPRECATED:
    text: DEPRECATED
    description: Discouraged for new use but still available.
    meaning: adms-status:Deprecated
  SUPERSEDED:
    text: SUPERSEDED
    description: Replaced by a newer version of this entity.
    todos:
    - Is 'superseded' permissible value needed? Keep for now, remove later if unsure.
    notes:
    - Mapped as close_mappings, not meaning. ADMS collapses supersession into Deprecated,
      which is already the exact meaning of DEPRECATED, and two values sharing one
      meaning URI would be indistinguishable in RDF.
    comments:
    - Neither ADMS nor PSO defines a supersession status, so this value is minted
      in the nexus namespace rather than aligned to an external vocabulary.
    close_mappings:
    - adms-status:Deprecated
  WITHDRAWN:
    text: WITHDRAWN
    description: Removed / no longer available.
    meaning: adms-status:Withdrawn

```
</details>

</div>
```
