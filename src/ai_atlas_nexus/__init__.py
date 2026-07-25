import os


# workaround for txtai
os.environ["KMP_DUPLICATE_LIB_OK"] = "True"
os.environ["OMP_NUM_THREADS"] = "1"

from .ai_risk_ontology import *


def __getattr__(name):
    if name == "AIAtlasNexus":
        from .library import AIAtlasNexus

        return AIAtlasNexus
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")


def __dir__():
    return sorted(set(globals()) | {"AIAtlasNexus"})
