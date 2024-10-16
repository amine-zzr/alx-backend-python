#!/usr/bin/env python3
"""
This module defines an asynchronous comprehension that collects
10 random numbers generated by an asynchronous generator.
"""

from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collects 10 random numbers using async comprehension over async_generator.

    Returns:
        A list of 10 float numbers generated by async_generator.
    """
    return [num async for num in async_generator()]
