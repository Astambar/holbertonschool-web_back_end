#!/usr/bin/env python3
""" 100-lfu_cache.py """
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ Classe LFUCache qui hérite de BaseCaching """

    def __init__(self):
        """ Méthode constructeur """
        super().__init__()
        # Liste pour suivre l'ordre d'utilisation des clés
        self.usage_order = []
        # Dictionnaire pour suivre la fréquence d'utilisation des clés
        self.key_frequencies = {}

    def put(self, key, item):
        """ Méthode qui ajoute une paire clé-valeur au cache """
        if key is None or item is None:
            return

        cache_length = len(self.cache_data)
        # Vérifiez si le cache est plein
        # et si la clé n'est pas déjà dans le cache
        if (
            cache_length >= BaseCaching.MAX_ITEMS
            and key not in self.cache_data
        ):
            # Trouvez la clé avec la fréquence d'utilisation la plus basse
            min_frequency = min(self.key_frequencies.values())
            key_freq_items = self.key_frequencies.items()
            min_frequency_keys = [
                cache_key
                for cache_key, frequency in key_freq_items
                if frequency == min_frequency
            ]
            # S'il y a plusieurs clés avec la même fréquence la plus basse,
            # trouvez la clé la moins récemment utilisée parmi elles
            if len(min_frequency_keys) > 1:
                lru_lfu = {}
                for cache_key in min_frequency_keys:
                    lru_lfu[cache_key] = self.usage_order.index(cache_key)
                discard_index = min(lru_lfu.values())
                discard_key = self.usage_order[discard_index]
            else:
                discard_key = min_frequency_keys[0]

            # Supprimez la clé la moins fréquemment utilisée
            # (ou la moins récemment utilisée parmi elles)
            print("DISCARD: {}".format(discard_key))
            del self.cache_data[discard_key]
            del self.usage_order[self.usage_order.index(discard_key)]
            del self.key_frequencies[discard_key]

        # Mettez à jour la fréquence d'utilisation
        # et l'ordre d'utilisation de la clé
        self.key_frequencies[key] = self.key_frequencies.get(key, 0) + 1
        if key in self.usage_order:
            del self.usage_order[self.usage_order.index(key)]
        self.usage_order.append(key)
        # Ajoutez la paire clé-valeur au cache
        self.cache_data[key] = item

    def get(self, key):
        """ Méthode qui obtient une valeur du cache à partir d'une clé """
        if key is not None and key in self.cache_data.keys():
            # Mettez à jour la fréquence d'utilisation
            # et l'ordre d'utilisation de la clé
            del self.usage_order[self.usage_order.index(key)]
            self.usage_order.append(key)
            self.key_frequencies[key] += 1
            return self.cache_data[key]
        return None
