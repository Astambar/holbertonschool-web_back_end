#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
fonction  de fonction multiplicateur
& nombre a multiplier
"""

from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """_summary_

    Args:
        lst (Iterable[Sequence]): _description_

    Returns:
        List[Tuple[Sequence, int]]: _description_
    """
    return [(i, len(i)) for i in lst]
