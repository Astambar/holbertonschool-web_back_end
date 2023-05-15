#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
fonction  de fonction multiplicateur
& nombre a multiplier
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """_make_multiplier_

    Args:
        multiplier (float): _description_

    Returns:
        Callable[[float], float]: _description_
    """
    def multiply_by(n: float) -> float:
        return n * multiplier
    return multiply_by
