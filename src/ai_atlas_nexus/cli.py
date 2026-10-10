"""The ``ran`` command line.

``ran query`` lists the records of the AI risk ontology. Its commands are built
from the LinkML schema each time the command line starts: one command for each
class whose records the schema's tree root can hold, and one option for each
slot of that class. A class or slot added to the schema therefore needs no change
here. The records are loaded only when a query runs, so ``--help`` stays quick.
"""

import inspect
import json
import os
from enum import Enum
from functools import lru_cache
from typing import Any, Callable, Optional

import typer
import yaml
from linkml_runtime import SchemaView
from linkml_runtime.linkml_model.meta import SlotDefinition
from pydantic_core import to_jsonable_python

from ai_atlas_nexus.ai_risk_ontology.datamodel import ai_risk_ontology
from ai_atlas_nexus.toolkit.data_utils import load_yamls_to_container


SCHEMA_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "ai_risk_ontology/schema/ai-risk-ontology.yaml",
)

# The Python type of an option, chosen by the LinkML type at the root of the
# slot's range. Every other type, a reference to another record and an enum
# without values are given as text.
OPTION_TYPES = {
    "integer": int,
    "float": float,
    "double": float,
    "decimal": float,
    "boolean": bool,
}

QUERY_HELP = (
    "List the records of one class of the AI risk ontology. Each command is the "
    "name of a class in lower case, and it lists the records of that class and of "
    "its subclasses. Each option filters on one slot of the class and keeps the "
    "slot's name from the schema. Repeat the option of a multivalued slot to "
    "require every value. Give --id to print the one record with that identifier."
)

QUERY_EXAMPLES = """\b
Examples:
  ran query risk --isDefinedByTaxonomy ibm-risk-atlas
  ran query risk --id atlas-toxic-output --format yaml
  ran query action --hasRelatedRisk credo-risk-036
"""


class OutputFormat(str, Enum):
    """The formats a query can print."""

    json = "json"
    yaml = "yaml"


@lru_cache(maxsize=1)
def schema_view() -> SchemaView:
    """The schema that ships with the package, found as ``AIAtlasNexus`` finds it."""
    return SchemaView(SCHEMA_PATH)


def command_name(class_name: str) -> str:
    """The command of a class is its name in lower case: RiskControl is riskcontrol."""
    return class_name.lower()


def query_classes(view: SchemaView) -> list[str]:
    """The classes that get a command, in the order of their command names.

    A class gets a command when the schema's tree root can hold its records,
    which means that it is the range of one of the root's slots or a subclass of
    one, and when it is not abstract.
    """
    classes = view.all_classes()
    root = next(name for name, definition in classes.items() if definition.tree_root)
    ranges = {slot.range for slot in view.class_induced_slots(root)}
    names = {
        name
        for range_name in ranges
        if range_name in classes
        for name in view.class_descendants(range_name)
        if not classes[name].abstract
    }
    return sorted(names, key=command_name)


def build_query_app(view: SchemaView) -> typer.Typer:
    """The ``query`` app, with one command for each class in ``query_classes``."""
    query = typer.Typer(
        help=QUERY_HELP,
        epilog=QUERY_EXAMPLES,
        no_args_is_help=True,
        rich_markup_mode=None,
    )
    enums = {
        name: Enum(
            name, {value: value for value in definition.permissible_values}, type=str
        )
        for name, definition in view.all_enums().items()
        if definition.permissible_values
    }
    for class_name in query_classes(view):
        description = view.get_class(class_name).description
        command = _query_command(view, class_name, enums)
        query.command(name=command_name(class_name), help=_paragraph(description))(
            command
        )
    return query


def _query_command(
    view: SchemaView, class_name: str, enums: dict[str, type[Enum]]
) -> Callable[..., None]:
    """The function behind the command of one class.

    typer reads the options of a command from the signature of its function and
    their types from the function's annotations, so both are set here: one
    keyword parameter for each slot that can filter, and one for the format.
    """
    parameters = [
        _option(view, slot, enums)
        for slot in view.class_induced_slots(class_name)
        if _can_filter(view, slot)
    ]
    parameters.append(
        inspect.Parameter(
            "format",
            inspect.Parameter.KEYWORD_ONLY,
            default=typer.Option(
                OutputFormat.json, "--format", help="Print JSON or YAML."
            ),
            annotation=OutputFormat,
        )
    )
    identifier = view.get_identifier_slot(class_name)

    def command(format: OutputFormat, **filters: Any) -> None:
        filters = {name: value for name, value in filters.items() if value is not None}
        records = [
            record for record in _records(class_name) if _matches(record, filters)
        ]
        if identifier is None or identifier.name not in filters:
            _print([_data(record) for record in records], format)
        elif records:
            _print(_data(records[0]), format)
        else:
            value = filters[identifier.name]
            typer.echo(f"No {class_name} has the {identifier.name} {value}.", err=True)
            raise typer.Exit(code=1)

    command.__signature__ = inspect.Signature(parameters)
    command.__annotations__ = {
        parameter.name: parameter.annotation for parameter in parameters
    }
    return command


def _option(
    view: SchemaView, slot: SlotDefinition, enums: dict[str, type[Enum]]
) -> inspect.Parameter:
    """The keyword parameter of one slot, named exactly as the slot is."""
    if slot.range in enums:
        option_type = enums[slot.range]
    elif slot.range in view.all_types():
        option_type = OPTION_TYPES.get(view.type_ancestors(slot.range)[-1], str)
    else:
        option_type = str
    flag = f"--{slot.name}"
    if option_type is bool:
        flag = f"{flag}/--no-{slot.name}"
    help_text = _paragraph(slot.description) or ""
    annotation = Optional[option_type]
    if slot.multivalued:
        help_text = f"{help_text} Repeat it to require several values.".strip()
        annotation = Optional[list[option_type]]
    return inspect.Parameter(
        slot.name,
        inspect.Parameter.KEYWORD_ONLY,
        default=typer.Option(None, flag, help=help_text),
        annotation=annotation,
    )


def _can_filter(view: SchemaView, slot: SlotDefinition) -> bool:
    """A slot can filter when it holds values or identifiers, not nested objects."""
    range_class = view.all_classes().get(slot.range)
    if range_class is None or range_class.class_uri == "linkml:Any":
        return True
    return not view.is_inlined(slot)


def _paragraph(text: Optional[str]) -> Optional[str]:
    """A schema description as one paragraph, which the help then wraps."""
    return " ".join(text.split()) if text else None


@lru_cache(maxsize=1)
def _container() -> ai_risk_ontology.Container:
    """The packaged records, read once with the loader ``AIAtlasNexus`` uses."""
    return load_yamls_to_container(None)


def _records(class_name: str) -> list:
    """The records of a class and of its subclasses, from every slot of the container."""
    model = getattr(ai_risk_ontology, class_name)
    container = _container()
    return [
        record
        for collection in type(container).model_fields
        for record in getattr(container, collection) or []
        if isinstance(record, model)
    ]


def _matches(record: Any, filters: dict[str, Any]) -> bool:
    """A single value must equal the record's value, and the values of a
    repeated option must all be in the record's list."""
    for name, wanted in filters.items():
        value = to_jsonable_python(getattr(record, name, None))
        if isinstance(wanted, list):
            if not isinstance(value, list) or any(
                to_jsonable_python(item) not in value for item in wanted
            ):
                return False
        elif value != to_jsonable_python(wanted):
            return False
    return True


def _data(record: Any) -> dict:
    """A record as plain data, without the slots it leaves empty."""
    return record.model_dump(mode="json", exclude_none=True)


def _print(data: Any, format: OutputFormat) -> None:
    if format is OutputFormat.yaml:
        typer.echo(yaml.safe_dump(data, sort_keys=False, allow_unicode=True), nl=False)
    else:
        typer.echo(json.dumps(data, indent=2, ensure_ascii=False))


app = typer.Typer(
    help="AI Atlas Nexus on the command line.",
    no_args_is_help=True,
    rich_markup_mode=None,
)
app.add_typer(build_query_app(schema_view()), name="query")
