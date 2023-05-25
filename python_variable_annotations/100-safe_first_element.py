#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Bonne annotation pour un type indéfini en entrée
ainsi qu'un type indéfini ou None en sortie
"""

from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Renvoie le premier élément de la séquence d'entrée
    si elle n'est pas vide, sinon renvoie None.

    Args:
        lst (Sequence[Any]): La séquence d'entrée
                             dont le premier élément doit être renvoyé.

    Returns:
        Union[Any, None]: Le premier élément de la séquence
                          d'entrée si elle n'est pas vide, sinon None.
    """
    if lst:
        return lst[0]
    else:
        return None
