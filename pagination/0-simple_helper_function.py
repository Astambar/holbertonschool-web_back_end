#!/usr/bin/env python3
""" 0-simple_helper_function.py """


def index_range(page, page_size) -> tuple:
    """
    Cette fonction calcule les indices de début
    et de fin pour une page de données.
    page: le numéro de la page
    page_size: le nombre d'éléments par page
    """
    debut = (page - 1) * page_size
    fin = page * page_size
    return (debut, fin)
