#!/usr/bin/env python3
"""
This module defines an asynchronous generator that yields
random numbers between 0 and 10 after an asynchronous delay.
"""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Asynchronously generates 10 random numbers between 0 and 10,
    with a 1-second delay between each number.

    Yields:
        A float representing a random number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
