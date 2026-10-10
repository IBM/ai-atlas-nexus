"""The ``ran query`` command line, built from the schema."""

import json

import pytest
import yaml
from linkml_runtime import SchemaView
from typer.testing import CliRunner

from ai_atlas_nexus import AIAtlasNexus, cli


runner = CliRunner()


@pytest.fixture(scope="module")
def library():
    return AIAtlasNexus()


def _run(*args):
    return runner.invoke(cli.app, list(args), prog_name="ran")


def _json(*args):
    result = _run("query", *args)
    assert result.exit_code == 0, result.output
    return json.loads(result.stdout)


def _ids(*args):
    return {record["id"] for record in _json(*args)}


def _fail_to_load(*args):
    raise AssertionError("the records were loaded")


def test_help_lists_one_command_per_class():
    result = _run("query", "--help")
    assert result.exit_code == 0, result.output
    listing = result.output.split("Commands:\n")[1].split("\n\n")[0]
    commands = [line.split()[0] for line in listing.splitlines()]
    view = cli.schema_view()
    assert commands == [cli.command_name(name) for name in cli.query_classes(view)]
    assert {"action", "risk", "riskcontrol"} <= set(commands)


def test_help_and_usage_errors_do_not_load_the_records(monkeypatch):
    monkeypatch.setattr(cli, "_container", _fail_to_load)
    assert _run("query", "--help").exit_code == 0
    assert _run("query", "risk", "--help").exit_code == 0
    assert _run("query", "risk", "--hasLifecycleStatus", "bogus").exit_code == 2


@pytest.mark.parametrize(
    "args, expected",
    [
        (
            ["risk", "--isDefinedByTaxonomy", "ibm-risk-atlas"],
            lambda library: library.get_all_risks(taxonomy="ibm-risk-atlas"),
        ),
        (
            ["risk", "--descriptor", "amplified by agentic AI"],
            lambda library: library.query(
                "risks", descriptor="amplified by agentic AI"
            ),
        ),
        (["action"], lambda library: library.get_instances("action")),
    ],
    ids=["single-valued slot", "multivalued slot", "class in two collections"],
)
def test_filter_gives_the_count_the_library_gives(library, args, expected):
    count = len(expected(library))
    assert count > 0
    assert len(_json(*args)) == count


def test_repeated_option_requires_every_value(library):
    risk = next(
        risk for risk in library.get_all_risks() if len(risk.related_mappings or []) > 1
    )
    first, second = risk.related_mappings[:2]
    both = _ids("risk", "--related_mappings", first, "--related_mappings", second)
    assert risk.id in both
    assert both == _ids("risk", "--related_mappings", first) & _ids(
        "risk", "--related_mappings", second
    )


def test_id_prints_one_record(library):
    risk = library.get_all_risks(taxonomy="ibm-risk-atlas")[0]
    expected = risk.model_dump(mode="json", exclude_none=True)
    assert _json("risk", "--id", risk.id) == expected
    result = _run("query", "risk", "--id", risk.id, "--format", "yaml")
    assert result.exit_code == 0, result.output
    assert yaml.safe_load(result.stdout) == expected
    assert _run("query", "risk", "--id", "no-such-risk").exit_code == 1


def test_base_dir_adds_its_records_to_the_packaged_ones(tmp_path):
    (tmp_path / "terms.yaml").write_text(
        "entries:\n- id: example-term\n  name: Example term\n  type: Term\n"
    )
    base_dir = str(tmp_path)
    assert _ids("--base-dir", base_dir, "term") == _ids("term") | {"example-term"}
    assert _ids("--base-dir", base_dir, "risk") == _ids("risk")


def test_base_dir_must_be_a_directory(tmp_path, monkeypatch):
    monkeypatch.setattr(cli, "_container", _fail_to_load)
    a_file = tmp_path / "terms.yaml"
    a_file.write_text("entries: []\n")
    for path in (tmp_path / "missing", a_file):
        result = _run("query", "--base-dir", str(path), "risk")
        assert result.exit_code == 2
        assert "Invalid value for '--base-dir'" in result.output


def test_bad_enum_value_exits_2():
    result = _run("query", "risk", "--hasLifecycleStatus", "bogus")
    assert result.exit_code == 2
    assert "Invalid value for '--hasLifecycleStatus'" in result.output


def test_enum_without_values_takes_any_text():
    view = SchemaView(cli.SCHEMA_PATH)
    view.get_enum("LifecycleStatus").permissible_values.clear()
    query = cli.build_query_app(view)
    result = runner.invoke(query, ["risk", "--hasLifecycleStatus", "any text"])
    assert result.exit_code == 0, result.output
    assert json.loads(result.stdout) == []
