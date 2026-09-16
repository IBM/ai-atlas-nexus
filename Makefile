# The purpose of this makefile is to update pydantic classes and graph output

VERSION = $(shell git tag | tail -1)

MAKEFLAGS += --warn-undefined-variables

SCHEMA_NAME = ai-risk-ontology
LINKML_SCHEMA_NAME = ai-risk-ontology
SOURCE_SCHEMA_PATH = src/ai_atlas_nexus/ai_risk_ontology/schema
LINKML_GENERATORS = .linkml/generators.yaml
KG_DATA_PATH = src/ai_atlas_nexus/data/knowledge_graph
DATAMODEL_PATH = src/ai_atlas_nexus/ai_risk_ontology/datamodel

SHELL := bash
.SHELLFLAGS := -eu -o pipefail -c
.DEFAULT_GOAL := help
.DELETE_ON_ERROR:
.SUFFIXES:
.SECONDARY:

RUN=pipenv run

help: status
	@echo ""
	@echo "make test -- runs tests"
	@echo "make help -- show this help"
	@echo "make lift_mappings_from_tsv -- lift mappings from all tsv files to yaml directory."
	@echo "make compile_pydantic_model -- update pydantic classes"
	@echo "make regenerate_documentation -- regenerate the documentation"
	@echo "make regenerate_graph_output -- export the graph with all instances"
	@echo "make regenerate_owl_schema -- export the schema as OWL"
	@echo "make regenerate_project -- regenerate the LinkML project artefacts in project/ (targets of https://w3id.org/ai-atlas-nexus)"
	@echo "make regenerate_risk_atlas_as_tex -- export the IBM AI risk atlas as .tex"
	@echo "make regenerate_cypher_code -- export the graph with all instances to Cypher queries"
	@echo "make regenerate_graph_as_sigma_js_json -- export the graph with all instances to a Sigma js JSON"
	@echo "make lint_schema -- schema linter shortcut"
	@echo ""

status:
	@echo "Project: $(SCHEMA_NAME)"
	@echo "Datafolder: $(SOURCE_SCHEMA_PATH)"

regenerate_documentation:
	gen-doc -d docs/ontology $(SOURCE_SCHEMA_PATH)/${LINKML_SCHEMA_NAME}.yaml

lift_mappings_from_tsv:
	python ./src/ai_atlas_nexus/ai_risk_ontology/util/lifting/import_entity_mappings.py

compile_pydantic_model:
	gen-pydantic --meta auto $(SOURCE_SCHEMA_PATH)/${LINKML_SCHEMA_NAME}.yaml > ${DATAMODEL_PATH}/ai_risk_ontology.py

regenerate_graph_output:
	python ./src/ai_atlas_nexus/ai_risk_ontology/util/export_graph.py

regenerate_owl_schema:
	gen-owl $(SOURCE_SCHEMA_PATH)/${LINKML_SCHEMA_NAME}.yaml --metadata-profile 'linkml' \
	--no-use-native-uris \
	--default-permissible-value-type 'http://www.w3.org/2004/02/skos/core#Concept' \
	> graph_export/owl/${LINKML_SCHEMA_NAME}_schema.ttl

# LinkML project artefacts in project/: the redirect targets of the persistent
# identifiers under https://w3id.org/ai-atlas-nexus/. Which generators run is
# configured in ${LINKML_GENERATORS}; add one there to publish it.
# The merged schema is what downstream projects import as nexus:ai-risk-ontology.
regenerate_project:
	mkdir -p project/linkml project/shacl
	gen-linkml --mergeimports -f yaml -o project/linkml/${LINKML_SCHEMA_NAME}.merged.linkml.yaml $(SOURCE_SCHEMA_PATH)/${LINKML_SCHEMA_NAME}.yaml
	gen-project --config-file ${LINKML_GENERATORS} -d project $(SOURCE_SCHEMA_PATH)/${LINKML_SCHEMA_NAME}.yaml
	gen-shacl project/linkml/${LINKML_SCHEMA_NAME}.merged.linkml.yaml > project/shacl/${LINKML_SCHEMA_NAME}.shacl.ttl

regenerate_risk_atlas_as_tex:
	python ./src/ai_atlas_nexus/ai_risk_ontology/util/export_risk_atlas_tex.py

regenerate_cypher_code:
	python ./src/ai_atlas_nexus/ai_risk_ontology/util/export_cypher.py

regenerate_graph_as_sigma_js_json:
	python ./src/ai_atlas_nexus/ai_risk_ontology/util/export_json_graph.py

lint_schema:
	linkml-lint $(SOURCE_SCHEMA_PATH)/${LINKML_SCHEMA_NAME}.yaml

test:
	pytest
