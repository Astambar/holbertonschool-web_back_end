#!/usr/bin/env python3
"""Module LRUCache qui définit la classe LRUCache.
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """Classe LRUCache qui implémente un cache LRU.
    """

    def __init__(self):
        """Initialise le cache.
        """
        super().__init__()
        self.cache_order = []

    def put(self, key: str, item: object) -> None:
        """Ajoute un élément dans le cache.

        Si la clé ou l'élément est None, ne fait rien.
        Si le cache est plein, évince l'élément le moins récemment utilisé.

        Args:
            key: clé de l'élément à ajouter.
            item: élément à ajouter.
        """
        if key in self.cache_order:
            self.cache_order.remove(key)

        if len(self.cache_data) == BaseCaching.MAX_ITEMS:
            least_recently_used_key = self.cache_order.pop()

            del self.cache_data[least_recently_used_key]

            print("DISCARD: {}".format(least_recently_used_key))
        if key and item:
            self.cache_order.insert(0, key)
            self.cache_data[key] = item

    def get(self, key: str) -> object:
        """Récupère un élément du cache en utilisant sa clé.

        Si la clé est None ou si elle n'est pas présente dans le cache,
        renvoie None.

        Args:
            key: clé de l'élément à récupérer.

        Returns:
            L'élément associé à la clé ou None si la clé n'est pas présente.
        """
        if key and key in self.cache_data:
            self.cache_order.remove(key)
            self.cache_order.insert(0, key)
            return self.cache_data[key]

        return None
