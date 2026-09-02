---
type: Playbook
id: https://w3id.org/ai-atlas-nexus/knowledge/playbooks/knowledge-sources
title: Knowledge Sources Map
description: The map of where this bundle's knowledge comes from - which repository paths and external URLs yield which LOKF concepts, and how to re-check each on a refresh run.
genre: reference
resource: https://github.com/IBM/ai-atlas-nexus
generated:
  by: process:lokf-librarian
  at: "2026-09-02T16:35:47Z"
references:
  - https://w3id.org/ai-atlas-nexus/knowledge/services/python-library
  - https://w3id.org/ai-atlas-nexus/knowledge/services/ran-extension-cli
  - https://w3id.org/ai-atlas-nexus/knowledge/datasets/ai-risk-ontology
  - https://w3id.org/ai-atlas-nexus/knowledge/datasets/knowledge-graph
  - https://w3id.org/ai-atlas-nexus/knowledge/datasets/graph-export
  - https://w3id.org/ai-atlas-nexus/knowledge/references/eu-ai-act
  - https://w3id.org/ai-atlas-nexus/knowledge/references/ibm-ai-risk-atlas
  - https://w3id.org/ai-atlas-nexus/knowledge/playbooks/contributing-a-taxonomy
  - https://w3id.org/ai-atlas-nexus/knowledge/playbooks/regenerate-artifacts
  - https://w3id.org/ai-atlas-nexus/knowledge/tutorials/quickstart
  - https://w3id.org/ai-atlas-nexus/knowledge/glossary/cot-template
  - https://w3id.org/ai-atlas-nexus/knowledge/org/ai-atlas-nexus-team
  - https://w3id.org/ai-atlas-nexus/knowledge/org/ibm
---

# Knowledge Sources

This is the librarian's scrape map. Steady-state refresh runs re-verify each row instead of re-discovering the repository; update this file whenever the repository's knowledge geography changes.

| Source | Yields | Re-check by |
|--------|--------|-------------|
| `pyproject.toml`, `README.md` | project name/description/authors, [python-library](../services/python-library.md) facts | diff manifest fields, README Features/Links sections |
| `src/ai_atlas_nexus/library.py`, `src/ai_atlas_nexus/blocks/` | [python-library](../services/python-library.md) (Service) | confirm `AIAtlasNexus` entry point and block/inference modules still exist |
| `src/ai_atlas_nexus/extension.py` + `[project.scripts]` | [ran-extension-cli](../services/ran-extension-cli.md) (Service) | confirm the console script declaration |
| `src/ai_atlas_nexus/ai_risk_ontology/schema/*.yaml` | [ai-risk-ontology](../datasets/ai-risk-ontology.md) (Dataset), [eu-ai-act](../references/eu-ai-act.md) (Reference) | list schema modules and the root import closure; confirm schema `version` and the `nexus` namespace `https://w3id.org/ai-atlas-nexus/` |
| `src/ai_atlas_nexus/ai_risk_ontology/datamodel/`, `.../util/` | generated Pydantic classes and lifting tooling - recorded inside [ai-risk-ontology](../datasets/ai-risk-ontology.md) and [regenerate-artifacts](regenerate-artifacts.md), no concepts of their own | confirm they are still generated/driven by the `Makefile` |
| `src/ai_atlas_nexus/data/knowledge_graph/*.yaml` + its `README.md` | [knowledge-graph](../datasets/knowledge-graph.md) (Dataset) and one Reference per headline taxonomy | walk the README's file/source table; each data file's `documentation` entries carry name + url |
| `src/ai_atlas_nexus/data/templates/*.json` | [cot-template](../glossary/cot-template.md) (GlossaryTerm) | confirm the `*_cot.json` few-shot template files |
| `src/ai_atlas_nexus/data/mappings/*.tsv` (source) and `src/ai_atlas_nexus/data/knowledge_graph/mappings/*.yaml` (lifted) | SSSOM cross-taxonomy mappings - recorded inside [knowledge-graph](../datasets/knowledge-graph.md) | confirm both folders; the YAML is generated from the TSV by `make lift_mappings_from_tsv` |
| `graph_export/` | [graph-export](../datasets/graph-export.md) (Dataset) | confirm each format's exact export file and the README |
| `Makefile` | [regenerate-artifacts](regenerate-artifacts.md) (Playbook) | diff `make help` target list against the playbook's bullets |
| `docs/concepts/Contributing_a_taxonomy.md`, `CONTRIBUTING.md` | [contributing-a-taxonomy](contributing-a-taxonomy.md) (Playbook) | re-read the doc's section list |
| `docs/concepts/Chain_of_thought_templates.md` | [cot-template](../glossary/cot-template.md) (GlossaryTerm) | re-read the definition paragraph |
| `docs/concepts/IBM_AI_Risk_Atlas.md` | [ibm-ai-risk-atlas](../references/ibm-ai-risk-atlas.md) (Reference) | re-read for taxonomy scope changes |
| `docs/examples/notebooks/` | [quickstart](../tutorials/quickstart.md) (Tutorial); further notebooks **not yet individually mapped** | list notebooks; split into per-notebook Tutorials when warranted |
| `.github/CODEOWNERS.md`, `pyproject.toml` authors | [ai-atlas-nexus-team](../org/ai-atlas-nexus-team.md), [ibm](../org/ibm.md) (Organization) | diff owners/authors |
| `LICENSE` | the bundle's own `license` (Apache-2.0) in `index.md` | confirm the repository licence has not changed |

## Consciously left out (for now)

- `resources/*.csv` raw extracts - recorded as provenance inside [knowledge-graph](../datasets/knowledge-graph.md) rather than as separate Dataset concepts; `resources/images/` and `resources/source/architecture.pptx` are presentation assets.
- Knowledge-graph sources beyond the README's headline list (AIUC-1, CSIRO RAI, Eticas, ShieldGemma, OECD/UN/Australia/IBM ethics principles, Hugging Face ML tasks) - the folder README is their authoritative table; promote to Reference concepts as needed.
- `docs/concepts/architecture.md` and `docs/concepts/Risk_Categorization.md` - future `Explanation` concepts; `docs/concepts/index.md` is a nav stub.
- `src/ai_atlas_nexus/toolkit/` - internal helpers (logging, validation, job/data utils) with no standalone knowledge value.
- `docs/installation/`, `docs/usage/`, `docs/reference/`, `tests/`, `mkdocs.yml`, and the CI workflows (`.github/workflows/regenerate-on-merge.yaml`, plus this bundle's own `knowledge-*.yaml`) - operational docs/config, no concepts yet.
- Sibling repositories ([ai-atlas-nexus-demos](https://github.com/IBM/ai-atlas-nexus-demos), [ai-atlas-nexus-extensions](https://github.com/ibm/ai-atlas-nexus-extensions)) - external to this bundle's scope.
