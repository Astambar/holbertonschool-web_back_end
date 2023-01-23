#!/usr/bin/env python3
"""make_multiplier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return a function that multiplies a float by multiplier.

    Args:
        multiplier (float): the float to multiply by

    Returns:
        Callable[[float], float]: function that multiplies a float
    """

    def multiply_by(n: float) -> float:
        return n * multiplier
    return multiply_by
