#!/usr/bin/python3
""" 2-lifo_cache.py """
import base_caching


class LIFOCache(base_caching.BaseCaching):
    """ LIFOCache """

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """
        Ajoute un élément au cache en utilisant le comportement LIFO
        (dernier entré, premier sorti).
        Si le cache est plein, le dernier élément
        ajouté sera supprimé pour faire de la place pour le nouvel élément.
        """
        if not key or not item:
            return

        if key in self.cache_data:
            del self.cache_data[key]

        if len(self.cache_data) == self.MAX_ITEMS:
            k = list(self.cache_data.keys()).pop()
            del self.cache_data[k]
            print("DISCARD: {}".format(k))

        self.cache_data[key] = item

    def get(self, key):
        """
        Récupère un élément du cache à partir de sa clé.
        Retourne None si l'élément n'est pas présent dans le cache.
        """
        return self.cache_data.get(key)
