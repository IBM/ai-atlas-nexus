---
type: Dataset
id: https://w3id.org/ai-atlas-nexus/knowledge/datasets/graph-export
title: Populated Graph Export
description: Pre-populated exports of the AI risk knowledge graph in YAML, OWL/Turtle, Cypher, JSON, and LaTeX formats, ready for download.
resource: https://github.com/IBM/ai-atlas-nexus/tree/main/graph_export
generated:
  by: process:lokf-librarian
  at: "2026-09-02T16:11:53Z"
distribution:
  - access_url: https://github.com/IBM/ai-atlas-nexus/blob/main/graph_export/yaml/ai-risk-ontology.yaml
    name: Full graph (YAML)
    media_type: application/yaml
  - access_url: https://github.com/IBM/ai-atlas-nexus/blob/main/graph_export/owl/ai-risk-ontology_schema.ttl
    name: Schema (OWL/Turtle)
    media_type: text/turtle
  - access_url: https://github.com/IBM/ai-atlas-nexus/blob/main/graph_export/cypher/ai-risk-ontology.cypher
    name: Cypher queries to populate a graph database
    media_type: text/plain
  - access_url: https://github.com/IBM/ai-atlas-nexus/blob/main/graph_export/json/ai-risk-ontology-sigma.json
    name: Sigma.js JSON export
    media_type: application/json
  - access_url: https://github.com/IBM/ai-atlas-nexus/blob/main/graph_export/latex/ibm-ai-risk-atlas-risks.tex
    name: LaTeX export of the IBM AI Risk Atlas risks
    media_type: application/x-tex
derivedFrom:
  - https://w3id.org/ai-atlas-nexus/knowledge/datasets/knowledge-graph
  - https://w3id.org/ai-atlas-nexus/knowledge/datasets/ai-risk-ontology
references:
  - https://w3id.org/ai-atlas-nexus/knowledge/playbooks/regenerate-artifacts
---

# Overview

`graph_export/` holds downloadable, regenerable projections of the ontology plus its instance data. They are produced from the LinkML sources by the repository `Makefile` targets (`make regenerate_graph_output`, `regenerate_owl_schema`, `regenerate_cypher_code`, `regenerate_graph_as_sigma_js_json`, `regenerate_risk_atlas_as_tex`) - see the [Regenerate repository artifacts](../playbooks/regenerate-artifacts.md) playbook.
