from collections.abc import Mapping
from typing import Any, Optional, Union

import jsonschema
from jsonschema.exceptions import ValidationError


# Validate instance data against a json schema
def validate(instance: Any, schema: Optional[Union[Mapping, bool]] = None):
    """Validate an instance against the given json schema.

    Args:
        instance (Any): The instance to validate
        schema (Optional[Union[Mapping, bool]], optional): The schema to validate with. Defaults to None.
    Returns:
        str: A string describing parsing error.
    """
    try:
        jsonschema.validate(instance, schema=schema)
        return None
    except ValidationError as e:
        return e.message
