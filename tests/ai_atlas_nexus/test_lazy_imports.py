import subprocess
import sys
import unittest


HEAVY_MODULES = ("txtai", "torch", "transformers", "openai")

LIBRARY_MODULES = ("linkml_runtime", "sssom_schema", "jinja2")


def _run_check(setup, modules):
    check = (
        "import sys; %s; "
        "loaded = [m for m in %r if m in sys.modules]; "
        "assert not loaded, 'loaded: ' + ', '.join(loaded)"
    ) % (setup, modules)
    return subprocess.run(
        [sys.executable, "-c", check],
        capture_output=True,
        text=True,
    )


class TestLazyImports(unittest.TestCase):
    """Heavy inference/mapping dependencies must not load at package import time."""

    def test_package_import_does_not_load_heavy_modules(self):
        # Run in a fresh interpreter because other tests in this process may
        # already have loaded the heavy modules.
        result = _run_check("import ai_atlas_nexus", HEAVY_MODULES)
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_package_import_does_not_load_library(self):
        result = _run_check("import ai_atlas_nexus", LIBRARY_MODULES)
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_class_access_does_not_load_heavy_modules(self):
        result = _run_check(
            "from ai_atlas_nexus import AIAtlasNexus", HEAVY_MODULES
        )
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_risk_mapping_import_does_not_load_heavy_modules(self):
        result = _run_check(
            "from ai_atlas_nexus.blocks.risk_mapping import RiskMapper",
            HEAVY_MODULES,
        )
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_class_is_importable(self):
        result = subprocess.run(
            [
                sys.executable,
                "-c",
                "import ai_atlas_nexus; "
                "assert ai_atlas_nexus.AIAtlasNexus.__name__ == 'AIAtlasNexus'; "
                "assert 'AIAtlasNexus' in dir(ai_atlas_nexus)",
            ],
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
