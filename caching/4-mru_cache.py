#!/usr/bin/python3
"""Module MRUCache qui définit la classe MRUCache.
"""

from collections import OrderedDict

BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """Classe MRUCache qui implémente un cache MRU.
    """

    def __init__(self):
        """Initialise le cache.
        """
        super().__init__()
        self.recently_used_keys = OrderedDict()

    def put(self, key: str, item: object) -> None:
        """Ajoute un élément dans le cache.

        Si la clé ou l'élément est None, ne fait rien.
        Si le cache est plein, évince l'élément le plus récemment utilisé.

        Args:
            key: clé de l'élément à ajouter.
            item: élément à ajouter.
        """
        if not key or not item:
            return

        self.cache_data[key] = item
        self.recently_used_keys[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            discarded_key = next(iter(self.recently_used_keys))
            del self.cache_data[discarded_key]
            print("DISCARD:", discarded_key)

        if len(self.recently_used_keys) > BaseCaching.MAX_ITEMS:
            self.recently_used_keys.popitem(last=False)

        self.recently_used_keys.move_to_end(key, False)

    def get(self, key: str) -> object:
        """Récupère un élément du cache en utilisant sa clé.

        Si la clé est None ou si elle n'est pas présente dans le cache,
        renvoie None.

        Args:
            key: clé de l'élément à récupérer.

        Returns:
            L'élément associé à la clé ou None si la clé n'est pas présente.
        """
        if key in self.cache_data:
            self.recently_used_keys.move_to_end(key, False)
            return self.cache_data[key]

        return None
