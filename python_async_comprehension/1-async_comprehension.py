#!/usr/bin/env python3
"""
2-measure_runtime.py
"""
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Cette fonction utilise une compréhension de liste asynchrone pour renvoyer
    une liste de nombres générés par la fonction async_generator.
    """
    return [i async for i in async_generator()]
