#!/usr/bin/env python3
"""1-simple_pagination.py"""
import csv
from typing import List


def index_range(page : int, page_size : int) -> tuple:
    """
    Cette fonction calcule les indices de début et de fin pour une page de données.
    page: le numéro de la page
    page_size: le nombre d'éléments par page
    """
    debut = (page - 1) * page_size
    fin = page * page_size
    return (debut, fin)


class Server:
    """Classe Server pour paginer une base de données de noms de bébés populaires"""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Jeu de données mis en cache"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Renvoie la page appropriée du jeu de données"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        index_debut, index_fin = index_range(page, page_size)
        return self.dataset()[index_debut:index_fin]
