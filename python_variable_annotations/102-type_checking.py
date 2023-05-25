#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Bonne annotation pour un type indéfini en entrée
ainsi qu'un type indéfini ou None en sortie
"""

from typing import Tuple, List
"""_typing import_

# Tuple: Un type générique qui représente un tuple de longueur fixe
         contenant des éléments de types spécifiques.
# List: Un type générique qui représente une liste contenant des éléments
        de types spécifiques.
"""


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Renvoie une liste agrandie en répétant
    chaque élément de `lst` `factor` fois.

    Args:
        lst (Tuple): Le tuple d'entrée dont les éléments doivent être répétés.
        factor (int, optional): Le nombre de fois que chaque élément
        doit être répété. Par défaut à 2.

    Returns:
        List: La liste agrandie en répétant
        chaque élément de `lst` `factor` fois.

    Exemple:
        >>> zoom_array((1, 2, 3), 2)
        [1, 1, 2, 2, 3, 3]
    """
    zoomed_in = []
    for item in lst:
        for i in range(factor):
            zoomed_in.append(item)
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(tuple(array))

zoom_3x = zoom_array(tuple(array), int(3.0))
