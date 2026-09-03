---
type: Playbook
id: https://w3id.org/ai-atlas-nexus/knowledge/playbooks/regenerate-artifacts
title: Regenerate Repository Artifacts
description: How to regenerate the generated artifacts - Pydantic datamodel, documentation, graph exports, OWL schema, Cypher, Sigma.js JSON, and LaTeX - from the LinkML sources with make.
genre: how-to
resource: https://github.com/IBM/ai-atlas-nexus/blob/main/Makefile
generated:
  by: process:lokf-librarian
  at: "2026-09-02T15:57:00Z"
about:
  - https://w3id.org/ai-atlas-nexus/knowledge/datasets/ai-risk-ontology
  - https://w3id.org/ai-atlas-nexus/knowledge/datasets/graph-export
---

# Overview

Run `make` (or `make help`) in the repository root. Key targets from the `Makefile`:

- `make compile_pydantic_model` - update the generated Pydantic classes under `ai_risk_ontology/datamodel/`.
- `make regenerate_documentation` - regenerate the LinkML schema docs into `docs/ontology/`.
- `make regenerate_graph_output` - export the graph with all instances (`graph_export/yaml/`).
- `make regenerate_owl_schema` - export the schema as OWL (`graph_export/owl/`).
- `make regenerate_cypher_code` - export instances as Cypher queries (`graph_export/cypher/`).
- `make regenerate_graph_as_sigma_js_json` - export a Sigma.js JSON (`graph_export/json/`).
- `make regenerate_risk_atlas_as_tex` - export the IBM AI Risk Atlas as LaTeX (`graph_export/latex/`).
- `make lift_mappings_from_tsv` - lift mappings from TSV files into the YAML directory.
- `make lint_schema` / `make test` - schema linter and tests.
