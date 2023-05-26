#!/usr/bin/env python3
"""Module BasicCache qui définit la classe BasicCache.
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Classe BasicCache qui hérite de BaseCaching.
    """
    def put(self, key: str, item: object) -> None:
        """Ajoute un élément dans le cache.

        Si la clé ou l'élément est None, ne fait rien.

        Args:
            key: clé de l'élément à ajouter.
            item: élément à ajouter.
        """
        if key is None or item is None:
            return
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
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
