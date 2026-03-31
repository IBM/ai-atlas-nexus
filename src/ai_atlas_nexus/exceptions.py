import traceback
from typing import List, Optional

from ai_atlas_nexus.toolkit.logging import configure_logger


LOGGER = configure_logger(__name__)


def handle_exception(
    exceptions: Optional[List[str]] = None,
):
    def decorator(func):

        def wrapper(*args, **kwargs):

            # Call the actual function
            try:
                event = func(*args, **kwargs)
            except Exception as e:
                if isinstance(e, tuple(exceptions)):
                    LOGGER.error(f"{e.name}: {e.message}")
                    return None
                else:
                    raise e

            return event

        return wrapper

    return decorator


class BaseException(Exception):

    def __init__(self, name, message, *args, resolution=None, **kwargs):
        self.name = name
        self.message = message
        self.resolution = resolution
        super().__init__(*args, **kwargs)


class RiskInferenceError(BaseException):

    def __init__(self, message, *args, **kwargs):
        super().__init__("RiskInferenceError", message, *args, **kwargs)
