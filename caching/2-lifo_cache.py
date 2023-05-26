#!/usr/bin/python3
"""Module LIFOCache qui définit la classe LIFOCache.
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """Classe LIFOCache qui implémente un cache LIFO.
    """

    def __init__(self):
        """Initialise le cache.
        """
        super().__init__()

    def put(self, key: str, item: object) -> None:
        """Ajoute un élément dans le cache.

        Si la clé ou l'élément est None, ne fait rien.
        Si le cache est plein, évince l'élément le plus récent.

        Args:
            key: clé de l'élément à ajouter.
            item: élément à ajouter.
        """
        if not key or not item:
            return

        if key in self.cache_data:
            del self.cache_data[key]

        keys = list(self.cache_data.keys())
        if len(keys) == self.MAX_ITEMS:
            removed_key = keys.pop()
            del self.cache_data[removed_key]
            print("DISCARD: {}".format(removed_key))

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
        return self.cache_data.get(key, None)
