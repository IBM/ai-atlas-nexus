---
type: Reference
id: https://w3id.org/ai-atlas-nexus/knowledge/references/eu-ai-act
title: EU AI Act
description: The European Union's Artificial Intelligence Act, whose vocabulary is modelled as a dedicated module of the AI Risk Ontology.
resource: https://eur-lex.europa.eu/eli/reg/2024/1689/oj
sameAs:
  - http://data.europa.eu/eli/reg/2024/1689/oj
generated:
  by: process:lokf-librarian
  at: "2026-09-02T16:11:53Z"
verified:
  - by: human:noelmcloughlin
    at: "2026-09-02T16:18:39Z"
sources:
  - resource: https://github.com/IBM/ai-atlas-nexus/blob/main/src/ai_atlas_nexus/ai_risk_ontology/schema/eu_ai_act.yaml
    title: eu_ai_act.yaml (LinkML vocabulary module)
---

# Overview

The **EU AI Act** vocabulary is modelled in the schema module `eu_ai_act.yaml` (schema id `https://w3id.org/ai-atlas-nexus/eu_ai_act`), which references bodies such as the EU AI Office. The `resource` above is the Act's ELI landing page in EUR-Lex (Regulation (EU) 2024/1689), and `sameAs` carries the canonical [ELI](https://eur-lex.europa.eu/eli-register/about.html) URI minted by the EU Publications Office, which resolves to that page. Neither URL is recorded in this repository - the schema module cites only the [EU AI Office](https://digital-strategy.ec.europa.eu/en/policies/ai-office) - so both were supplied by the librarian and confirmed by a maintainer; the repository is the authority only for how the Act is modelled, not for the Act's content.
