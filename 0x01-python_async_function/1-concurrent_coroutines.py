#!/usr/bin/env python3
"""
This module defines an asynchronous coroutine `wait_n` that spawns multiple
instances of wait_random concurrently and returns the delays in ascending order
"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns `wait_random` n times with the specified max_delay.

    Args:
        n (int): The number of times to spawn `wait_random`.
        max_delay (int): The maximum delay for each `wait_random` call.

    Returns:
        List[float]: List of delays in ascending order.
    """
    delays: List[float] = []
    for i in range(n):
        delay = await wait_random(max_delay)
        delays.append(delay)

    # Build the list of delays in ascending order without using `sort()`
    result: List[float] = []
    while delays:
        smallest: float = min(delays)
        result.append(smallest)
        delays.remove(smallest)

    return result
