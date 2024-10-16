#!/usr/bin/env python3
"""
This module defines a coroutine to measure the total runtime
of running async_comprehension four times in parallel.
"""

import asyncio
import time
from typing import List
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Executes async_comprehension four times and measures the total runtime.

    Returns:
        A float representing the total time taken to execute the coroutines.
    """
    start_time = time.perf_counter()

    await asyncio.gather(*[async_comprehension() for _ in range(4)])

    total_runtime = time.perf_counter() - start_time
    return total_runtime
