#!/usr/bin/env python3
"""
This module defines an asynchronous coroutine `wait_random` that waits
for a random delay between 0 and a given maximum number of seconds.
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for random delay between 0 and max_delay.

    Args:
        max_delay (int): Maximum number of seconds to wait. Defaults to 10.

    Returns:
        float: The random delay in seconds.
    """
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
