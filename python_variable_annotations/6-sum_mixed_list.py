#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" somme d'une liste de float & de int """

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """_sum_mixed_list_

    Args:
        mxd_lst (List[Union[int, float]]): _description_

    Returns:
        float: _description_
    """
    return sum(mxd_lst)
