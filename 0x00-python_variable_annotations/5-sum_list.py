#!/usr/bin/env python3
"""sum_list
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Return the sum of all elements in the list.

    Args:
        input_list (List[float]): a list of floats.

    Returns:
        float: the sum of all elements in the list.
    """
    return sum(input_list)
