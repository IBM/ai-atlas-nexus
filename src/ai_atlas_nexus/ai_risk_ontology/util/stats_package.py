#!/usr/bin/env python3

import argparse
import json
from collections import Counter
from datetime import datetime
from pathlib import Path

from rich.console import Console
from rich.table import Table

from ai_atlas_nexus import AIAtlasNexus


def compute_graph_stats():
    """
    Compute some entity and association statistics from the AIAtlasNexus.

    Returns:
        tuple[Counter, Counter]
            Tuple of (entity_counts, association_counts)
    """
    nexus = AIAtlasNexus()
    explorer = nexus._atlas_explorer

    # Entity counts:
    all_ids = list(explorer._id_cache.keys())
    entity_breakdown = explorer.arrange_ids_by_type(all_ids)
    entity_counts = Counter({k: len(v) for k, v in entity_breakdown.items()})

    # Association counts, but excluding literal/property fields
    id_set = set(all_ids)
    assoc_counts = Counter()
    literal_fields = {
        "id",
        "name",
        "tag",
        "description",
        "url",
        "version",
        "status",
        "type",
        "broader",
        "narrower",
    }

    for obj in explorer._id_cache.values():
        for field_name in type(obj).model_fields:
            if field_name in literal_fields:
                continue

            val = getattr(obj, field_name, None)
            if val is None:
                continue

            if isinstance(val, str) and val in id_set:
                assoc_counts[field_name] += 1
            elif isinstance(val, list):
                for item in val:
                    if isinstance(item, str) and item in id_set:
                        assoc_counts[field_name] += 1

    return entity_counts, assoc_counts


def print_stats_tables(entities, associations):
    """
    Output the statistics tables to the console

    Args:
        entities: Counter
            Entities in graph
        associations: Counter
            Associations in graph
    Returns:
        None
    """

    console = Console()

    entity_table = Table(
        title="Entity Statistics",
        show_header=True,
        header_style="bold magenta",
    )
    entity_table.add_column("Entity Type", style="cyan")
    entity_table.add_column("Count", justify="right", style="green")

    for label, count in entities.most_common():
        entity_table.add_row(label, str(count))

    entity_table.add_row(
        "[bold]Total[/bold]", f"[bold]{sum(entities.values())}[/bold]"
    )

    assoc_table = Table(
        title="Association Statistics",
        show_header=True,
        header_style="bold magenta",
    )
    assoc_table.add_column("Relationship Type", style="cyan")
    assoc_table.add_column("Count", justify="right", style="green")

    for rel_type, count in associations.most_common():
        assoc_table.add_row(rel_type, str(count))

    assoc_table.add_row(
        "[bold]Total[/bold]", f"[bold]{sum(associations.values())}[/bold]"
    )

    console.print()
    console.print(entity_table)
    console.print()
    console.print(assoc_table)
    console.print()


def write_stats_json(entities, associations, output_path):
    """Write statistics to a JSON file.

    Args:
        entities: Counter
        associations: Counter
        output_path: Path

    Returns:
        None
    """
    stats = {
        "source": "AIAtlasNexus package",
        "generated_at": datetime.now().isoformat(),
        "entities": dict(entities),
        "associations": dict(associations),
        "totals": {
            "entity_types": len(entities),
            "total_entities": sum(entities.values()),
            "association_types": len(associations),
            "total_associations": sum(associations.values()),
        },
    }

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(stats, f, indent=2)


def main():
    parser = argparse.ArgumentParser(
        description="Generate statistics from the AIAtlasNexus"
    )
    parser.add_argument(
        "--output",
        default="graph_export/stats_package.json",
        help="Path to write JSON stats (default: graph_export/stats_package.json)",
    )

    args = parser.parse_args()
    output_path = Path(args.output)

    entities, associations = compute_graph_stats()

    print_stats_tables(entities, associations)
    write_stats_json(entities, associations, output_path)

    console = Console()
    console.print(f"Stats written to {output_path}")

    return 0


if __name__ == "__main__":
    exit(main())
