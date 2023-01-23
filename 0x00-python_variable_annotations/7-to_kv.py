#!/usr/bin/env python3
"""to_kv
"""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return a tuple with k and v squared.

    Args:
        k (str): string
        v (Union[int, float]): int or float

    Returns:
        Tuple[str, float]: tuple with k and v squared
    """
    return (k, v*v)
