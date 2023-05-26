#!/usr/bin/env python3
"""
2-measure_runtime.py
"""
import time
import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Cette fonction mesure le temps d'exécution de quatre appels à la fonction
    async_comprehension en utilisant asyncio.gather.
    """
    start = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end = time.perf_counter()
    return (end - start)
