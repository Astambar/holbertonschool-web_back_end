#!/usr/bin/env python3
""" 0-async_generator.py """
import asyncio
import random
import typing
Generator = typing.Generator
sleep = asyncio.sleep
uniform = random.uniform


async def async_generator() -> Generator[float, None, None]:
    """_summary_

    Yields:
        Generator[float, None, None]: _description_
    """
    for i in range(10):
        await sleep(1)
        yield uniform(0, 10)
