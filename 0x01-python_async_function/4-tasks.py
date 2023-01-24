#!/usr/bin/env python3
""" 4-tasks.py """
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """_summary_

    Args:
        n (int): _description_
        max_delay (int): _description_

    Returns:
        List[float]: _description_
    """
    floatlist = []
    for i in range(n):
        floatlist.append(task_wait_random(max_delay))
    return [await i for i in asyncio.as_completed(floatlist)]
