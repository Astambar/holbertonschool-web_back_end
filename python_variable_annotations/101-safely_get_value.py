#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Bonne annotation pour un type indéfini en entrée
ainsi qu'un type indéfini ou None en sortie
"""

from typing import Mapping, Any, Union, TypeVar
"""_typing import explication_
# Mapping: Un type générique qui représente un dictionnaire
           contenant des clés et des valeurs de types spécifiques.
# Any: Un type spécial qui indique que n'importe quel type
       de valeur est acceptable.
# Union: Un type générique qui indique qu'une valeur
         peut être de l'un des types spécifiés.
# TypeVar: Un type générique qui permet de définir
           des types variables pour les fonctions génériques.
"""

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """
    Renvoie la valeur associée à la clé donnée
    dans le dictionnaire d'entrée si elle existe,
    sinon renvoie la valeur par défaut.

    Args:
        dct (Mapping): Le dictionnaire d'entrée
                       dont la valeur associée à la clé doit être renvoyée.
        key (Any): La clé dont la valeur associée doit être renvoyée.
        default (Union[T, None], optional):
                La valeur par défaut à renvoyer
                si la clé n'existe pas dans le dictionnaire.
                Par défaut à None.

    Returns:
        Union[Any, T]: La valeur associée à la clé donnée
        dans le dictionnaire d'entrée si elle existe,
        sinon la valeur par défaut.
    """
    if key in dct:
        return dct[key]
    else:
        return default
