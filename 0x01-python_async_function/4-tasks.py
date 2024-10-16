#!/usr/bin/env python3
"""
This module defines an asynchronous coroutine `task_wait_n` that spawns
multiple tasks using `task_wait_random` and returns the delays
in ascending order of completion.
"""

import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns `task_wait_random` n times with the specified max_delay and returns
    the list of delays in ascending order based on the completion time.

    Args:
        n (int): The number of times to spawn `task_wait_random`.
        max_delay (int): The maximum delay for each `task_wait_random` call.

    Returns:
        List[float]: List of delays in ascending order based on completion time
    """
    # Create n tasks using task_wait_random
    tasks = [task_wait_random(max_delay) for _ in range(n)]

    # Collect delays in the order of task completion
    delays: List[float] = []
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays
