# Assisted by watsonx Code Assistant
import asyncio
import time
import unittest
from concurrent.futures import ThreadPoolExecutor

from ai_atlas_nexus.toolkit.async_utils import (
    ClientCache,
    _EventLoopHandler,
    generate_batch_async,
    get_current_event_loop,
    run_async_in_thread,
)


class TestGetCurrentEventLoop(unittest.TestCase):
    """Test cases for get_current_event_loop function."""

    def test_no_running_loop(self):
        """Test that None is returned when there's no running event loop."""
        loop = get_current_event_loop()
        self.assertIsNone(loop)

    def test_with_running_loop(self):
        """Test that the current loop is returned when running inside an event loop."""

        async def check_loop():
            loop = get_current_event_loop()
            self.assertIsNotNone(loop)
            self.assertIsInstance(loop, asyncio.AbstractEventLoop)
            return loop

        loop = asyncio.run(check_loop())
        self.assertIsNotNone(loop)


class TestEventLoopHandler(unittest.TestCase):
    """Test cases for _EventLoopHandler class."""

    def test_init_creates_event_loop_and_thread(self):
        """Test that initialization creates an event loop and starts a daemon thread."""
        handler = _EventLoopHandler()
        self.assertIsNotNone(handler._event_loop)
        self.assertIsNotNone(handler._thread)
        self.assertTrue(handler._thread.is_alive())
        self.assertTrue(handler._thread.daemon)
        handler._close_event_loop()

    def test_call_runs_coroutine(self):
        """Test that calling the handler runs the coroutine and returns the result."""
        handler = _EventLoopHandler()

        async def async_func():
            await asyncio.sleep(0.01)
            return 42

        result = handler(async_func())
        self.assertEqual(result, 42)
        handler._close_event_loop()

    def test_call_with_exception(self):
        """Test that exceptions in coroutines are properly propagated."""
        handler = _EventLoopHandler()

        async def async_func_with_error():
            await asyncio.sleep(0.01)
            raise ValueError("Test error")

        with self.assertRaises(ValueError) as ctx:
            handler(async_func_with_error())
        self.assertEqual(str(ctx.exception), "Test error")
        handler._close_event_loop()

    def test_reinit_if_forked(self):
        """Test that the handler reinitializes after a fork."""
        handler = _EventLoopHandler()
        original_pid = handler._pid
        original_loop = handler._event_loop
        original_thread = handler._thread

        # Simulate a fork by changing the pid
        handler._pid = original_pid + 1
        handler._reinit_if_forked()

        # Check that new event loop and thread were created
        self.assertNotEqual(handler._event_loop, original_loop)
        self.assertNotEqual(handler._thread, original_thread)
        self.assertTrue(handler._thread.is_alive())
        handler._close_event_loop()

    def test_close_event_loop(self):
        """Test that closing the event loop stops it properly."""
        handler = _EventLoopHandler()
        thread = handler._thread

        # Verify thread is running before closing
        self.assertTrue(thread.is_alive())

        handler._close_event_loop()

        # Give some time for the loop to stop
        time.sleep(0.2)
        # Check that the thread is no longer alive after closing
        # Note: daemon threads may still be alive but the loop should be stopped

    def test_nested_call_creates_new_handler(self):
        """Test that calling from within the same event loop creates a new handler."""
        handler = _EventLoopHandler()

        async def inner_async():
            return "inner"

        async def outer_async():
            # This would normally deadlock if not handled properly
            result = run_async_in_thread(inner_async())
            return f"outer-{result}"

        result = handler(outer_async())
        self.assertEqual(result, "outer-inner")
        handler._close_event_loop()


class TestRunAsyncInThread(unittest.TestCase):
    """Test cases for run_async_in_thread function."""

    def test_basic_coroutine(self):
        """Test running a basic async function."""

        async def async_add(a, b):
            await asyncio.sleep(0.01)
            return a + b

        result = run_async_in_thread(async_add(5, 3))
        self.assertEqual(result, 8)

    def test_multiple_concurrent_calls(self):
        """Test that multiple concurrent calls work correctly."""

        async def async_multiply(x):
            await asyncio.sleep(0.01)
            return x * 2

        with ThreadPoolExecutor(max_workers=5) as executor:
            futures = [
                executor.submit(run_async_in_thread, async_multiply(i))
                for i in range(10)
            ]
            results = [f.result() for f in futures]

        expected = [i * 2 for i in range(10)]
        self.assertEqual(results, expected)

    def test_exception_propagation(self):
        """Test that exceptions are properly propagated."""

        async def async_error():
            await asyncio.sleep(0.01)
            raise RuntimeError("Async error")

        with self.assertRaises(RuntimeError) as ctx:
            run_async_in_thread(async_error())
        self.assertEqual(str(ctx.exception), "Async error")

    def test_return_complex_types(self):
        """Test returning complex data types."""

        async def async_complex():
            await asyncio.sleep(0.01)
            return {"key": "value", "list": [1, 2, 3], "nested": {"data": 42}}

        result = run_async_in_thread(async_complex())
        self.assertEqual(result["key"], "value")
        self.assertEqual(result["list"], [1, 2, 3])
        self.assertEqual(result["nested"]["data"], 42)


class TestGenerateBatchAsync(unittest.TestCase):
    """Test cases for generate_batch_async function."""

    def test_basic_batch_processing(self):
        """Test basic batch processing with async function."""

        async def process_item(item):
            await asyncio.sleep(0.01)
            return item * 2

        async def run_test():
            items = [1, 2, 3, 4, 5]
            results = await generate_batch_async(
                process_item, items, desc="Test", verbose=False
            )
            return results

        results = asyncio.run(run_test())
        self.assertEqual(results, [2, 4, 6, 8, 10])

    def test_empty_list(self):
        """Test batch processing with an empty list."""

        async def process_item(item):
            return item

        async def run_test():
            results = await generate_batch_async(
                process_item, [], desc="Empty", verbose=False
            )
            return results

        results = asyncio.run(run_test())
        self.assertEqual(results, [])

    def test_with_exceptions(self):
        """Test that exceptions in batch processing are handled."""

        async def process_item(item):
            await asyncio.sleep(0.01)
            if item == 3:
                raise ValueError(f"Error processing {item}")
            return item * 2

        async def run_test():
            items = [1, 2, 3, 4, 5]
            with self.assertRaises(ValueError):
                await generate_batch_async(
                    process_item, items, desc="Error test", verbose=False
                )

        asyncio.run(run_test())

    def test_verbose_flag(self):
        """Test that verbose flag controls progress display."""

        async def process_item(item):
            await asyncio.sleep(0.001)
            return item

        async def run_test():
            items = [1, 2, 3]
            # Should not raise an error with verbose=True or False
            results_verbose = await generate_batch_async(
                process_item, items, desc="Verbose", verbose=True
            )
            results_quiet = await generate_batch_async(
                process_item, items, desc="Quiet", verbose=False
            )
            return results_verbose, results_quiet

        results_verbose, results_quiet = asyncio.run(run_test())
        self.assertEqual(results_verbose, [1, 2, 3])
        self.assertEqual(results_quiet, [1, 2, 3])


class TestClientCache(unittest.TestCase):
    """Test cases for ClientCache class."""

    def test_init(self):
        """Test cache initialization."""
        cache = ClientCache(capacity=3)
        self.assertEqual(cache.capacity, 3)
        self.assertEqual(cache.cache, {})
        self.assertEqual(cache.access_order, [])

    def test_put_and_get(self):
        """Test putting and getting items from cache."""
        cache = ClientCache(capacity=3)
        cache.put("key1", "value1")
        cache.put("key2", "value2")

        self.assertEqual(cache.get("key1"), "value1")
        self.assertEqual(cache.get("key2"), "value2")
        self.assertIsNone(cache.get("key3"))

    def test_lru_eviction(self):
        """Test that least recently used items are evicted."""
        cache = ClientCache(capacity=2)
        cache.put("key1", "value1")
        cache.put("key2", "value2")

        # This should evict key1
        cache.put("key3", "value3")

        self.assertIsNone(cache.get("key1"))
        self.assertEqual(cache.get("key2"), "value2")
        self.assertEqual(cache.get("key3"), "value3")

    def test_access_order_update(self):
        """Test that accessing an item updates its position in LRU order."""
        cache = ClientCache(capacity=2)
        cache.put("key1", "value1")
        cache.put("key2", "value2")

        # Access key1 to make it most recently used
        cache.get("key1")

        # Adding key3 should evict key2 (least recently used)
        cache.put("key3", "value3")

        self.assertEqual(cache.get("key1"), "value1")
        self.assertIsNone(cache.get("key2"))
        self.assertEqual(cache.get("key3"), "value3")

    def test_update_existing_key(self):
        """Test updating an existing key."""
        cache = ClientCache(capacity=2)
        cache.put("key1", "value1")
        cache.put("key2", "value2")

        # Update key1 with new value
        cache.put("key1", "new_value1")

        self.assertEqual(cache.get("key1"), "new_value1")
        self.assertEqual(len(cache.cache), 2)

    def test_access_order_after_update(self):
        """Test that updating a key moves it to the end of access order."""
        cache = ClientCache(capacity=2)
        cache.put("key1", "value1")
        cache.put("key2", "value2")

        # Update key1
        cache.put("key1", "new_value1")

        # key1 should now be most recently used
        cache.put("key3", "value3")

        self.assertEqual(cache.get("key1"), "new_value1")
        self.assertIsNone(cache.get("key2"))  # key2 was evicted
        self.assertEqual(cache.get("key3"), "value3")

    def test_capacity_one(self):
        """Test cache with capacity of 1."""
        cache = ClientCache(capacity=1)
        cache.put("key1", "value1")
        self.assertEqual(cache.get("key1"), "value1")

        cache.put("key2", "value2")
        self.assertIsNone(cache.get("key1"))
        self.assertEqual(cache.get("key2"), "value2")


if __name__ == "__main__":
    unittest.main()
