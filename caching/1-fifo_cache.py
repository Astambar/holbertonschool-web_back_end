#!/usr/bin/env python3
"""
Module FIFOCache qui définit la classe FIFOCache.
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    Classe FIFOCache qui implémente un cache FIFO.
    """

    def __init__(self):
        """
        Initialise le cache.
        """
        super().__init__()
        self.cache_data = {}
        self.keys = []

    def put(self, key: str, item: object) -> None:
        """
        Ajoute un élément dans le cache.

        Si la clé ou l'élément est None, ne fait rien.
        Si le cache est plein, évince l'élément le plus ancien.

        Args:
            key: clé de l'élément à ajouter.
            item: élément à ajouter.
        """
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            discarded_key = self.keys.pop(0)
            self.cache_data.pop(discarded_key)
            print("DISCARD: {}".format(discarded_key))

        self.cache_data[key] = item
        self.keys.append(key)

    def get(self, key: str) -> object:
        """
        Récupère un élément du cache en utilisant sa clé.

        Si la clé est None ou si elle n'est pas présente dans le cache,
        renvoie None.

        Args:
            key: clé de l'élément à récupérer.

        Returns:
            L'élément associé à la clé ou None si la clé n'est pas présente.
        """
        if key is None or key not in self.cache_data:
            return None

        return self.cache_data[key]
