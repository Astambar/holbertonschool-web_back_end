#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
détermine Typing object Iterable
& forme de sortie attendu Tuple Sequence , int
"""

from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """_element_length_

    Args:
        lst (Iterable[Sequence]): _description_

    Returns:
        List[Tuple[Sequence, int]]: _description_
    """
    return [(i, len(i)) for i in lst]
