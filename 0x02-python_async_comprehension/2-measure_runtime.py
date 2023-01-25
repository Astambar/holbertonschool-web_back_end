#!/usr/bin/env python3
""" 2-measure_runtime.py """
import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension
perf_counter = time.perf_counter
gather = asyncio.gather


async def measure_runtime() -> float:
    """_summary_

    Returns:
        float: _description_
    """
    start = perf_counter()
    await gather(*(async_comprehension() for i in range(4)))
    end = perf_counter()
    return (end - start)
