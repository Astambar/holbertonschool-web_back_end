#!/usr/bin/env python3
"""sum_mixed_list
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Return the sum of all elements in the list.

    Args:
        mxd_lst (List[Union[int, float]]): a list of integers and floats.

    Returns:
        float: the sum of all elements in the list.
    """
    return sum(mxd_lst)
