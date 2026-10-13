"""
Check that the identifiers in the SSSOM mapping files are CURIEs with declared prefixes.

The SSSOM/TSV format requires each value of an entity reference slot, such as
subject_id, object_id, author_id or creator_id, to be a CURIE whose prefix the
file's curie_map declares, unless the prefix is built in. `sssom validate` from
sssom 0.4.21 misses two faults that later make `sssom convert` fail: it never
checks a prefix that contains a hyphen (mapping-commons/sssom-py#673, fixed by
#676), and it passes a value that is not a CURIE at all, such as an e-mail
address (mapping-commons/sssom-py#675). This check covers both until a sssom
release does.

Usage: python check_mapping_prefixes.py [FILE.tsv ...]
With no arguments it checks every TSV in src/ai_atlas_nexus/data/mappings.
"""

# Standard Library
import sys
from collections import Counter
from pathlib import Path

# Third Party
import yaml  # installed with sssom
from sssom.constants import SSSOMSchemaView
from sssom.context import SSSOM_BUILT_IN_PREFIXES


MAP_DIR = Path(__file__).resolve().parents[3] / "data" / "mappings"


def read_sssom_tsv(path):
    """Return the metadata, column names and numbered rows of an SSSOM/TSV file."""
    lines = Path(path).read_text(encoding="utf-8").splitlines()
    header = []
    for start, line in enumerate(lines):
        if not line.startswith("#"):
            break
        header.append(line.lstrip("#").rstrip())
    metadata = yaml.safe_load("\n".join(h for h in header if h)) or {}
    columns = lines[start].split("\t")
    rows = [
        (number, line.split("\t"))
        for number, line in enumerate(lines[start + 1 :], start=start + 2)
    ]
    return metadata, columns, rows


def problem_with(value, known_prefixes):
    """Say what is wrong with one entity reference, or return None if nothing is."""
    prefix, colon, local = value.partition(":")
    if prefix in ("http", "https") and local.startswith("//"):
        return f"{value!r} is a URL, not a CURIE"
    if not colon or not prefix or not local or " " in value:
        return f"{value!r} is not a CURIE"
    if prefix not in known_prefixes:
        return f"prefix {prefix!r} is not declared in the curie_map"
    return None


def check_file(path, entity_reference_slots):
    """Return a list of problem lines for one mapping file."""
    metadata, columns, rows = read_sssom_tsv(path)
    known = set(metadata.get("curie_map") or {}) | set(SSSOM_BUILT_IN_PREFIXES)
    found = Counter()
    first_line = {}

    def check(slot, values, line):
        for value in values:
            value = value.strip()
            if not value:
                continue
            problem = problem_with(value, known)
            if problem:
                found[(slot, problem)] += 1
                first_line.setdefault((slot, problem), line)

    for slot in entity_reference_slots & set(metadata):
        value = metadata[slot]
        check(slot, value if isinstance(value, list) else [str(value)], "the header")
    for definition in metadata.get("extension_definitions") or []:
        for slot in ("property", "type_hint"):
            if definition.get(slot):
                check(f"extension_definitions {slot}", [definition[slot]], "the header")
    for slot in entity_reference_slots & set(columns):
        i = columns.index(slot)
        for number, cells in rows:
            if i < len(cells):
                check(slot, cells[i].split("|"), f"line {number}")

    report = []
    for (slot, problem), n in sorted(found.items()):
        count = f"{n} value" if n == 1 else f"{n} values"
        where = first_line[(slot, problem)]
        report.append(f"{slot}: {problem} ({count}, first in {where})")
    return report


def main(paths):
    paths = paths or sorted(MAP_DIR.glob("*.tsv"))
    slots = set(SSSOMSchemaView().entity_reference_slots)
    failed = 0
    for path in paths:
        problems = check_file(path, slots)
        print(f"{'FAIL' if problems else 'ok':4}  {Path(path).name}")
        for problem in problems:
            print(f"      {problem}")
        failed += bool(problems)
    print(
        f"{len(paths)} files checked, "
        f"{failed} with identifiers that are not declared CURIEs"
    )
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
