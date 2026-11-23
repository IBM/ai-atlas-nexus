# Migrating from 1.x to 2.0

AI Atlas Nexus 2.0 changes the ontology's public contract. The Python API
(`AIAtlasNexus` methods) is backwards compatible, and several methods were
added. The breaking changes are in the **generated datamodel**, the
**RDF/OWL/Cypher exports**, and a few **dependencies and behaviours**.

| If you use...                                            | Impact                                                     |
| -------------------------------------------------------- | ---------------------------------------------------------- |
| Only `AIAtlasNexus` methods on the bundled data          | Low. Check [Behaviour changes](#behaviour-changes).        |
| The Pydantic datamodel directly, or your own YAML data   | Medium. See [Datamodel](#datamodel-python).                |
| SPARQL, OWL, Cypher or JSON exports from `graph_export/` | High. See [RDF and graph exports](#rdf-and-graph-exports). |

## Datamodel (Python)

### Jurisdictions are now strict enums

`Jurisdiction`, `SupraNationalJurisdiction` and `SubnationalJurisdiction` are now real `Enum`s generated from `jurisdictions.yaml`, built from the DPV Location
vocabulary.

- `hasJurisdiction` accepts only ISO 3166-1 alpha-2 codes (`US`), ISO 3166-2
  subdivision codes (`US-CA`), supra-national unions (`EU`, `EEA`) and
  `International`. Other strings should fail Pydantic validation.
- **Action:** validate your own YAML or code. Replace values such as
  `"European Union"` with `EU`.

```python
# 1.x: any string was accepted
Policy(id="p", name="p", hasJurisdiction=["Europe"])
# 2.0: raises ValidationError. Use a code from jurisdictions.yaml
Policy(id="p", name="p", hasJurisdiction=["EU"])
```

### Class and slot changes

| Change                                                                                                                                                 | Action                                                                                             |
| ------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------- |
| `type` is now a slot on `Entity`. The default (e.g. `type="Risk"`) is unchanged.                                                                       | None for loading data. Code that introspects `linkml_meta` per class should read it from `Entity`. |
| `Certification` is no longer `abstract`.                                                                                                               | It can now be instantiated directly. Remove any code that relied on it being rejected.             |
| `Group.broader` and `Group.narrower` are now `Group` references (they were untyped). `broader` previously used the wrong `slot_uri` (`skos:narrower`). | Use group ids. Re-check any RDF consumers of `broader`.                                            |
| `hasPrinciple` now applies to any `Entry`, not only `Requirement`.                                                                                     | Additive.                                                                                          |
| `isProvidedBy` is now defined on `BaseAi` through `slot_usage` (range `AiProvider`). The Python type is still `Optional[str]`.                         | None in Python. The RDF predicate for AI systems is `airo:isProvidedBy`.                           |
| `hasCapability` no longer declares `inverse: implementsCapability`.                                                                                    | Do not rely on automatic inverse traversal. Query both directions explicitly.                      |

## RDF and graph exports

Several class and predicate URIs were changed to `nexus:` terms, and prefixes
were renamed. **SPARQL queries, SHACL shapes and mappings written against 1.x
exports will could stop matching.**

| Term                       | 1.x                  | 2.0                                                                 |
| -------------------------- | -------------------- | ------------------------------------------------------------------- |
| `CapabilityTaxonomy` class | `skos:ConceptScheme` | `nexus:CapabilityTaxonomy`                                          |
| `Vocabulary` class         | `skos:ConceptScheme` | `nexus:Vocabulary` (`skos:ConceptScheme` is now an `exact_mapping`) |
| `LLMIntrinsic` class       | `ai:Capability`      | `nexus:LLMIntrinsic` (`ai:Capability` is now a `broad_mapping`)     |
| `isDefinedByTaxonomy`      | `schema:isPartOf`    | `nexus:isDefinedByTaxonomy`                                         |
| `isDefinedByVocabulary`    | `schema:isPartOf`    | `nexus:isDefinedByVocabulary`                                       |
| Domain-membership slot     | `schema:isPartOf`    | `nexus:belongsToDomain`                                             |
| Capability to AI inverse   | `tech:hasCapability` | `nexus:possessedByAi`                                               |
| `hasImplementation`        | `schema:url`         | `nexus:hasImplementation`                                           |
| `hasUnitxtCard`            | `schema:url`         | `nexus:hasUnitxtCard`                                               |
| `Group.broader`            | `skos:narrower`      | `skos:broader`                                                      |
| Prefix `dpv-loc`           | `dpv-loc:`           | `dpv_loc:`                                                          |
| Prefix `dpv-risk`          | `dpv-risk:`          | `dpv_risk:`                                                         |
| Prefix `adms-status`       | `adms-status:`       | `adms_status:`                                                      |

The old `schema:` and `skos:` terms are kept as `broad_mappings` or
`exact_mappings` where there is a valid mapping. To find the old behaviour,
query the mapping annotations instead of the primary URI.

**Action:** search your queries for the old terms (e.g. `grep -rn "schema:isPartOf\|dpv-risk\|adms-status"`)
and update them. Regenerate any cached exports.

### Other export changes

- **Cypher:** strings are now escaped, and lists and booleans are emitted as
  real Cypher values. Properties that were quoted strings in 1.x may now be
  lists or booleans, and `cymple` is no longer used.
- **JSON graph:** multivalued scalar slots (e.g. `isCategorizedAs`) are now
  included as node attributes.
- **PyOxigraph explorer:** `get_all("Entry")` and similar class names now
  include subclasses, and collection keys are filtered by id. Results can be
  larger or ordered differently than in 1.x.
- `graph_export/` files are regenerated, so expect large diffs.

## Dependencies and packaging

- `cymple` is **removed**. If your code imported it, add it to your own
  dependencies.
- `chardet==5.2.0` is now `chardet>=5.2.0,<8`.
- `requests>=2.33.0` is required.
- The `vllm` extra now requires `vllm>=0.32.0`.
- `requires-python` is now `>=3.11,<=3.14.7`.
- The package declares a `setuptools` build backend and installs a new `ran`
  console script (alongside `ran-extension`).

## Behaviour changes

- **Prompt templates are sandboxed.** Templates are compiled in Jinja's
  `ImmutableSandboxedEnvironment`. Custom templates that call mutating or
  unsafe methods should now raise errors.
- **Curated mappings.** `load_curated_mappings` now drops rows with a `Not`
  predicate modifier and rows pointing at `sssom:NoTermFound`. Before, it only
  dropped `predicate_id == "noMatch"`. Evaluation ground truth derived from
  these files changes.
- **Load order.** YAML files are now loaded in sorted order, so results that
  depended on filesystem order are now deterministic.

## New in 2.0 (non-breaking)

- A `ran` CLI, including a schema-driven `ran query` command.
- `prompt_template` argument on `identify_risks_from_usecases` and
  `identify_risks_from_usecases_and_actions`.
- `ThirdPartyEvaluationEngagement`, `EvaluationStandardConformance` and
  `ConditionAssessment` classes, with `get_evaluation_engagements`,
  `get_evaluation_engagement` and `check_standard_conformance`.
- Data: AEF-1, RBI FREE-AI Seven Sutras, OWASP AST10 and MCP Top 10 linkages,
  and a the jurisdictions vocabulary.

## Upgrade checklist

1. Pin `ai-atlas-nexus>=2.0.0` and re-lock your environment.
2. Validate any custom YAML against the new schema. Pay particular attention to
   `hasJurisdiction` values.
3. Update SPARQL, SHACL and Cypher artifacts using the URI table above.
4. Re-run any evaluation that uses curated SSSOM mappings.
5. Review custom prompt templates for sandbox compatibility.
