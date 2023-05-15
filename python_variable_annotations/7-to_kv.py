#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tuple composé d'un str
& carré d'un float ou int retourner en tant que float
"""

from typing import tuple, Union


def to_kv(k: str, v: Union(int, float)) -> tuple(str, float):
    """_summary_

    Args:
        k (_type_): _description_
        float (_type_): _description_

    Returns:
        _tuple_: _description_
    """
    return str, v * v
