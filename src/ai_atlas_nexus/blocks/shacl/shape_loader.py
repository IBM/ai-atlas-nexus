import glob
import io
import logging
import os
from typing import Optional

import pyoxigraph


logger = logging.getLogger(__name__)

SH_CONSTRUCT = "http://www.w3.org/ns/shacl#construct"


def load_shapes(
    base_dir: Optional[str], container=None
) -> pyoxigraph.Store:
    """Load SHACL shapes into a pyoxigraph Store.

    Discovers shapes from two sources:
    - ``<base_dir>/shapes/`` directory: any ``*.ttl``, ``*.shacl``, ``*.n3`` files
    - YAML-embedded shapes: any ``shacl_shapes`` key in the loaded container's
      raw data, where each entry has a ``turtle`` string field

    Returns an empty Store when no shapes are found.
    """
    store = pyoxigraph.Store()

    if base_dir:
        shapes_dir = os.path.join(base_dir, "shapes")
        if os.path.isdir(shapes_dir):
            for pattern in ("*.ttl", "*.shacl", "*.n3"):
                for path in sorted(glob.glob(os.path.join(shapes_dir, pattern))):
                    _load_turtle_file(store, path)

    if container is not None:
        _load_yaml_shapes(store, container)

    return store


def _load_turtle_file(store: pyoxigraph.Store, path: str) -> None:
    try:
        with open(path, "rb") as fh:
            store.load(fh, format=pyoxigraph.RdfFormat.TURTLE)
        logger.debug("Loaded SHACL shapes from %s", path)
    except Exception as exc:
        logger.warning("Could not load shapes from %s: %s", path, exc)


def _load_yaml_shapes(store: pyoxigraph.Store, container) -> None:
    """Load inline Turtle snippets stored under a ``shacl_shapes`` container field."""
    raw = getattr(container, "shacl_shapes", None)
    if not raw:
        return
    for entry in raw:
        turtle_src = None
        if isinstance(entry, dict):
            turtle_src = entry.get("turtle")
        elif hasattr(entry, "turtle"):
            turtle_src = entry.turtle
        if turtle_src:
            try:
                store.load(
                    io.BytesIO(turtle_src.encode()),
                    format=pyoxigraph.RdfFormat.TURTLE,
                )
                logger.debug("Loaded inline SHACL shape from container")
            except Exception as exc:
                logger.warning("Could not parse inline SHACL shape: %s", exc)
