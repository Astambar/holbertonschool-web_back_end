#!/usr/bin/env python3
"""_summary_

Returns:
    _type_: _description_
"""
import asyncio
import random


async def wait_random(max_delay: int = 10):
    """_summary_

    Args:
        max_delay (int, optional): _description_. Defaults to 10.

    Returns:
        _type_: _description_
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
