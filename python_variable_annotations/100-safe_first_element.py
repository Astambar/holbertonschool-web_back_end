#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
détermine Typing object Iterable
& forme de sortie attendu Tuple Sequence , int
"""

from typing import Any, Sequence, Union


# The types of the elements of the input are not know
def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """_safe_first_element_

    Args:
        lst (Sequence[Any]): _description_

    Returns:
        Union[Any, None]: _description_
    """
    if lst:
        return lst[0]
    else:
        return None
