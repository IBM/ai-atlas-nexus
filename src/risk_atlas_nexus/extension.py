import importlib
import subprocess
import sys

from typer import Typer

from risk_atlas_nexus.toolkit.logging import configure_logger


app = Typer()
logger = configure_logger(__name__)


@app.callback()
def main() -> None:
    """
    RAN Extension CLI Application
    """


@app.command()
def install(extension_name: str) -> None:
    """
    Installs an extension

    :param extension_name: Name of the extension to install
    """
    logger.info("Installing extension: %s", extension_name)

    extension_location = (
        "git+ssh://git@github.com/dhavalsalwala/risk-atlas-nexus-extensions.git"
        + "#subdirectory="
        + extension_name
    )
    subprocess.check_call(
        [sys.executable, "-m", "pip", "install", extension_location]
    )  # nosec


class Extension:
    """
    Imports and loads a risk atlas nexus extension main class
    """

    @staticmethod
    def load(extension_name: str, *args, **kwargs) -> type:
        """Import the main extension class.

        Args:
            extension_name (str): a Risk Atlas Nexus extension name

        Raises:
            ModuleNotFoundError: if the main module is not present
            TypeError: if the main Extension class is not present

        Returns:
            type: The class for instantiation.
        """

        try:
            # Looking for an absolute class path
            module = importlib.import_module(extension_name.replace("-", "_") + ".main")
        except ModuleNotFoundError as no_mod:
            logger.error(f"Following extension not found: {extension_name}")
            logger.error(f"Install with: ran-extension install {extension_name}")
            sys.exit()

        try:
            extension_class = getattr(module, "Extension")
        except:
            raise TypeError("Extension class does not exist in the main module.")

        return extension_class(*args, **kwargs)
