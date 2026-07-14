import subprocess
import sys
import unittest


HEAVY_MODULES = ("txtai", "torch", "transformers", "openai")


class TestLazyImports(unittest.TestCase):
    """Heavy inference/mapping dependencies must not load at package import time."""

    def test_import_does_not_load_heavy_modules(self):
        # Run in a fresh interpreter because other tests in this process may
        # already have loaded the heavy modules.
        check = (
            "import sys; import ai_atlas_nexus; "
            "loaded = [m for m in %r if m in sys.modules]; "
            "assert not loaded, 'loaded at import time: ' + ', '.join(loaded)"
        ) % (HEAVY_MODULES,)
        result = subprocess.run(
            [sys.executable, "-c", check],
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
