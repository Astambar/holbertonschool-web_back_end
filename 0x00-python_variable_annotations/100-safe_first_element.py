#!/usr/bin/env python3
"""safe_first_element
"""
from typing import Any, Union, Sequence


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Return the first element of a sequence or None.

    Args:
        lst (Sequence[Any]): The input sequence.

    Returns:
        Union[Any, None]: The first element of the input sequence or None.
    """
    if lst:
        return lst[0]
    else:
        return None
