"""Helper for event loop management. Allows consistently running async code in sync functions."""

import asyncio
import os
import threading
from collections.abc import Coroutine
from typing import Any, List, Optional, TypeVar

from tqdm.asyncio import tqdm


R = TypeVar("R")


def get_current_event_loop():
    """Get the current event loop, or None if there isn't one."""
    try:
        return asyncio.get_running_loop()
    except RuntimeError:
        return None


class _EventLoopHandler:
    """A class that handles the event loop for async operations. Do not directly instantiate this. Use `run_async_in_thread`."""

    def _event_loop_setup(self):
        """Sets up the event loop and thread."""
        # This code lives in a helper function since both __init__ and _reinit_if_forked
        # will need to use it.
        self._pid = os.getpid()  # Store the pid in case users fork this process.
        self._event_loop = asyncio.new_event_loop()
        self._thread: threading.Thread = threading.Thread(
            target=self._event_loop.run_forever,
            daemon=True,
        )
        self._thread.start()

    def __init__(self):
        """Instantiates an EventLoopHandler. Used to ensure consistency when calling async code from sync code.

        Do not instantiate this class. Rely on the exported `run_async_in_thread` function.
        """
        self._event_loop_setup()

    def _reinit_if_forked(self) -> None:
        """Reinitialize the event loop and thread if we're in a forked child to prevent hanging on awaited tasks."""
        if os.getpid() != self._pid:
            # If the process has been forked, reset the event loop and thread.
            # Don't cleanup the parent's objects.
            self._event_loop_setup()

    def __del__(self):
        """Delete the event loop handler."""
        self._close_event_loop()

    def _close_event_loop(self) -> None:
        """Called when deleting the event loop handler. Cleans up the event loop and thread."""
        if self._event_loop:
            try:
                tasks = asyncio.all_tasks(self._event_loop)
                if tasks:
                    for task in tasks:
                        task.cancel()

                    async def finalize_tasks() -> None:
                        await asyncio.gather(*tasks, return_exceptions=True)

                    out = asyncio.run_coroutine_threadsafe(
                        finalize_tasks(), self._event_loop
                    )

                    # Wait for finalization to complete with timeout
                    try:
                        out.result(timeout=5)
                    except Exception:
                        pass
            except Exception:
                pass

            # Finally stop the event loop for this session.
            self._event_loop.stop()

    def __call__(self, co: Coroutine[Any, Any, R]) -> R:
        """Runs the coroutine in the event loop."""
        self._reinit_if_forked()
        if self._event_loop == get_current_event_loop():
            # If this gets called from the same event loop, launch in a separate thread to prevent blocking.
            return _EventLoopHandler()(co)
        return asyncio.run_coroutine_threadsafe(co, self._event_loop).result()


# Instantiate this class once. It will not be re-instantiated.
__event_loop_handler = _EventLoopHandler()


async def generate_batch_async(
    func,
    items,
    desc="Processing items",
    verbose: bool = True,
    concurrency_limit: Optional[int] = None,
) -> List[Any]:
    """Generate responses for multiple prompts concurrently using asyncio.gather."""
    # Create coroutines for all prompts
    coroutines = [func(item) for item in items]

    # Run all coroutines concurrently with asyncio.gather and tqdm progress bar
    return await tqdm.gather(
        *coroutines, desc=desc, total=len(items), disable=(not verbose)
    )


def run_async_in_thread(co: Coroutine[Any, Any, R]) -> R:
    """Call to run async code from synchronous code.

    This allows using async clients underneath sync code to improve
    concurrency. The async clients get bound to a specific event loop,
    so we maintain a single dedicated event loop for all async operations.

    Args:
        co: coroutine to run

    Returns:
        output of the coroutine
    """
    return __event_loop_handler(co)


class ClientCache:
    """LRU cache for async clients keyed by event loop ID."""

    def __init__(self, capacity: int = 2):
        """Initialize the cache with a maximum capacity."""
        self.capacity = capacity
        self.cache = {}
        self.access_order = []

    def get(self, key):
        """Get a client from the cache."""
        if key in self.cache:
            # Move to end (most recently used)
            self.access_order.remove(key)
            self.access_order.append(key)
            return self.cache[key]
        return None

    def put(self, key, value):
        """Put a client in the cache."""
        if key in self.cache:
            # Update existing
            self.access_order.remove(key)
        elif len(self.cache) >= self.capacity:
            # Evict least recently used
            lru_key = self.access_order.pop(0)
            del self.cache[lru_key]

        self.cache[key] = value
        self.access_order.append(key)


__all__ = ["run_async_in_thread", "get_current_event_loop", "ClientCache"]
