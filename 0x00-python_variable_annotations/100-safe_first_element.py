#!/usr/bin/env python3
"""safe_first_element
"""
from typing import Any, Union, Sequence, NoneType

def safe_first_element(lst: Sequence[Any]) -> Union[Any, NoneType]:
    """Return the first element of a sequence or None.

    Args:
        lst (Sequence[Any]): The input sequence.

    Returns:
        Union[Any, NoneType]: The first element of the input sequence or None.
    """
    if lst:
        return lst[0]
    else:
        return None
