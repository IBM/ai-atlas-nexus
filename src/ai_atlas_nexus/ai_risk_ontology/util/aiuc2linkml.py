# Standard Library
import csv
import os
from datetime import datetime

# Third Party
from linkml_runtime.dumpers import YAMLDumper

# Local
from ai_atlas_nexus.ai_risk_ontology import (
    Container,
    Documentation,
    Risk,
    RiskGroup,
    RiskTaxonomy,
)
from ai_atlas_nexus.data import get_data_path


def get_risks() -> list[dict]:
    with open("resources/AIUC-1_January_2026.csv") as csvfile:
        importer = csv.DictReader(csvfile)
        return [row for row in importer]


def convert_datetime_to_date(datetime_str: str) -> str:
    datetime_value = datetime.fromisoformat(datetime_str)
    return datetime_value.date().isoformat()


def create_container_object() -> Container:
    # Create paper
    documents = [
        Documentation(
            **{
                "id": "10a99803d8afd999",
                "name": "Foundation models: Opportunities, risks and mitigations",
                "description": "In this document we: Explore the benefits of foundation models, including their capability to perform challenging tasks, potential to speed up the adoption of AI, ability to increase productivity and the cost benefits they provide. Discuss the three categories of risk, including risks known from earlier forms of AI, known risks amplified by foundation models and emerging risks intrinsic to the generative capabilities of foundation models. Cover the principles, pillars and governance that form the foundation of IBM’s AI ethics initiatives and suggest guardrails for risk mitigation.",
                "url": "https://www.ibm.com/downloads/documents/us-en/10a99803d8afd656",
            }
        )
    ]

    # Create taxonomy
    taxonomies = [
        RiskTaxonomy(
            **{
                "id": "aiuc-1-principles",
                "name": "Artificial Intelligence Underwriting Company - 1",
                "description": "AIUC-1 is the world's first standard for AI agents. AIUC-1 covers data & privacy, security, safety, reliability, accountability and societal risks.",
                "url": "https://www.aiuc-1.com",
                "hasDocumentation": ["10a99803d8afd999"],
                "dateCreated": "2026-02-23",
                "dateModified": "2026-02-23",
            }
        )
    ]

    risks = get_risks()

    # Create risk groups
    risk_group_names = sorted(list(set([(risk["group"]) for risk in risks])))
    riskgroups = [
        RiskGroup(
            **{
                "id": "aiuc-1-principles-" + risk_group.lower().replace(" ", "-"),
                "name": risk_group.capitalize(),
                "isDefinedByTaxonomy": "aiuc-1-principles",
            }
        )
        for risk_group in risk_group_names
    ]

    # Create risks
    risk_objects = [
        Risk(
            **{
                "id": risk["id"],
                "name": risk["name"],
                "description": risk["description"],
                "url": f"https://www.aiuc-1.com/{risk["group"].lower().replace(" ","-")}/{risk["name"].lower()}",
                "isPartOf": "aiuc-1-principles-" + risk["group"].replace(" ", "-"),
                "isDefinedByTaxonomy": "aiuc-1-principles",
            }
        )
        for risk in risks
    ]

    # Create container
    container = Container(
        documents=documents,
        taxonomies=taxonomies,
        groups=riskgroups,
        entries=risk_objects,
    )
    return container


if __name__ == "__main__":
    with open(
        os.path.join(get_data_path(), "aiuc1_principles_data.yaml"),
        "+tw",
        encoding="utf-8",
    ) as output_file:
        container = create_container_object()
        print(YAMLDumper().dumps(container), file=output_file)
        output_file.close()
