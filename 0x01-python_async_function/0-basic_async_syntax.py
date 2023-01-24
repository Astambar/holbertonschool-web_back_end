#!/usr/bin/env python3
"""_summary_

Returns:
    _type_: _description_
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Wait for a random delay between 0 and
       max_delay seconds and return the delay value.

    Args:
        max_delay (int): The maximum delay in seconds. Default is 10.

    Returns:
        float: The delay value in seconds.
    """
    delay = random.random() * max_delay
    await asyncio.sleep(delay)
    return delay
