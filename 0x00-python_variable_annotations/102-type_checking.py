#!/usr/bin/env python3
"""zoom_array
"""
from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """_summary_

    Args:
        lst (Tuple): _description_
        factor (int, optional): _description_. Defaults to 2.

    Returns:
        List: _description_
    """
    zoomed_in = [
        item for i in range(factor)
        for item in lst
    ]
    return zoomed_in

array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
