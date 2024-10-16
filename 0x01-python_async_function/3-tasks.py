#!/usr/bin/env python3
"""
This module defines a function `task_wait_random` which returns an asyncio Task
for running the `wait_random` coroutine.
"""

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates and returns an asyncio Task for the `wait_random` coroutine.

    Args:
        max_delay (int): Max delay in seconds for the wait_random coroutine.

    Returns:
        asyncio.Task: A task object running `wait_random(max_delay)`.
    """
    return asyncio.create_task(wait_random(max_delay))
