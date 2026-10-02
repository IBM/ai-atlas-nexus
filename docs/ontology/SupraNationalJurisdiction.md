---
search:
  boost: 2.0
---

# Enum: SupraNationalJurisdiction

_Supra-national or intergovernmental jurisdiction, from the DPV Location vocabulary (https://w3id.org/dpv/loc). Values are members of dpv:SupraNationalUnion (e.g. EU, EEA), plus International._

<div data-search-exclude markdown="1">

URI: [dpv:SupraNationalUnion](https://w3id.org/dpv#SupraNationalUnion)

**Enum URI:** [dpv:SupraNationalUnion](https://w3id.org/dpv#SupraNationalUnion)

## Permissible Values

| Value         | Meaning       | Description                                                                      |
| ------------- | ------------- | -------------------------------------------------------------------------------- |
| EEA           | dpv-loc:EEA   | European Economic Area (EEA)                                                     |
| EEA30         | dpv-loc:EEA30 | EEA 30 Member States                                                             |
| EEA31         | dpv-loc:EEA31 | EEA 31 Member States                                                             |
| EU            | dpv-loc:EU    | European Union (EU)                                                              |
| EU27          | dpv-loc:EU27  | EU 27 Member States                                                              |
| EU28          | dpv-loc:EU28  | EU 28 Member States                                                              |
| International | None          | Explicitly global scope not attributable to any single country or recognised ... |

## See Also

- [https://w3id.org/dpv/loc](https://w3id.org/dpv/loc)

## Identifier and Mapping Information

### Schema Source

- from schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology

## LinkML Source

<details>
```yaml
name: SupraNationalJurisdiction
description: Supra-national or intergovernmental jurisdiction, from the DPV Location
  vocabulary (https://w3id.org/dpv/loc). Values are members of dpv:SupraNationalUnion
  (e.g. EU, EEA), plus International.
from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
see_also:
- https://w3id.org/dpv/loc
rank: 1000
enum_uri: dpv:SupraNationalUnion
permissible_values:
  EEA:
    text: EEA
    description: European Economic Area (EEA)
    meaning: dpv-loc:EEA
  EEA30:
    text: EEA30
    description: EEA 30 Member States
    meaning: dpv-loc:EEA30
  EEA31:
    text: EEA31
    description: EEA 31 Member States
    meaning: dpv-loc:EEA31
  EU:
    text: EU
    description: European Union (EU)
    meaning: dpv-loc:EU
  EU27:
    text: EU27
    description: EU 27 Member States
    meaning: dpv-loc:EU27
  EU28:
    text: EU28
    description: EU 28 Member States
    meaning: dpv-loc:EU28
  International:
    text: International
    description: Explicitly global scope not attributable to any single country or
      recognised regional body.
    aliases:
    - INTERNATIONAL
    - international

```
</details>

</div>
```
