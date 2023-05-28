#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
from typing import List, Dict


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
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Jeu de données mis en cache"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Jeu de données indexé par position de tri, en commençant par 0"""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Renvoie la page appropriée du jeu de données"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        index_debut, index_fin = index_range(page, page_size)
        return self.dataset()[index_debut:index_fin]

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> dict:
        """Renvoie un dictionnaire contenant des informations sur la pagination"""
        assert isinstance(index, int) and index >= 0
        assert isinstance(page_size, int) and page_size > 0

        indexed_dataset = self.indexed_dataset()
        data = []
        next_index = index
        for key in range(index, len(indexed_dataset)):
            if len(data) < page_size:
                if key in indexed_dataset:
                    data.append(indexed_dataset[key])
                    next_index = key + 1
            else:
                break

        return {
            'index': index,
            'next_index': next_index,
            'page_size': len(data),
            'data': data
        }
