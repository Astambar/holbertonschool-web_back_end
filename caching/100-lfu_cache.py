#!/usr/bin/env python3
"""Module LFUCache qui définit la classe LFUCache.
"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    Classe LFUCache qui implémente un cache LFU.

    Cette classe implémente un cache Least Frequently Used (LFU).
    Elle stocke un nombre limité d'éléments, évinçant les éléments
    les moins fréquemment utilisés lorsque le cache est plein.
    """

    def __init__(self):
        """Initialise le cache.
        """
        super().__init__()

        # Une liste pour stocker l'utilisation de chaque clé dans le cache
        self.usage_list = []

        # Un dictionnaire pour stocker la fréquence de chaque clé dans le cache
        self.frequency_dict = {}

    def put(self, key: str, item: object) -> None:
        """
        Ajoute un élément dans le cache avec la clé donnée.

        Si la clé ou l'élément est None, ne fait rien.
        Si le cache est plein, évince l'élément le moins fréquemment utilisé.

        Args:
            key: clé de l'élément à ajouter.
            item: élément à ajouter.
        """
        if key is None or item is None:
            return

        # Si le cache est plein et que la clé donnée
        # n'est pas dans le cache, trouve la clé
        # la moins fréquemment utilisée et l'évince.
        MAX_ITEMS = BaseCaching.MAX_ITEMS

        if len(self.cache_data) >= MAX_ITEMS and key not in self.cache_data:
            least_frequent_use = min(self.frequency_dict.values())
            keys_with_least_frequency = []

            for key, frequency in self.frequency_dict.items():
                if frequency == least_frequent_use:
                    keys_with_least_frequency.append(key)

            # S'il y a plus d'une clé avec la même fréquence minimale,
            # trouve la clé qui a été utilisée le moins récemment parmi elles.
            if len(keys_with_least_frequency) > 1:
                least_recently_used = {}

                for key in keys_with_least_frequency:
                    least_recently_used[key] = self.usage_list.index(key)

                key_to_discard = min(least_recently_used.values())
                key_to_discard = self.usage_list[key_to_discard]
            else:
                key_to_discard = keys_with_least_frequency[0]

            print("DISCARD: {}".format(key_to_discard))
            del self.cache_data[key_to_discard]
            del self.usage_list[self.usage_list.index(key_to_discard)]
            del self.frequency_dict[key_to_discard]

        # Met à jour la fréquence de la clé donnée
        if key in self.frequency_dict:
            self.frequency_dict[key] += 1
        else:
            self.frequency_dict[key] = 1

        # Met à jour l'utilisation de la clé donnée
        if key in self.usage_list:
            del self.usage_list[self.usage_list.index(key)]
        self.usage_list.append(key)

        # Ajoute l'élément dans le cache avec la clé donnée
        self.cache_data[key] = item

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
        # Si la clé n'est pas None et existe dans le dictionnaire cache_data
        if key is not None and key in self.cache_data.keys():
            # efface la clé de sa position actuelle dans la liste d'utilisation
            self.usage_list.remove(key)
            # Ajoute la clé à la fin de la liste d'utilisation
            self.usage_list.append(key)
            # Incrémente le compteur de fréquence pour la clé
            self.frequency_dict[key] += 1
            # Renvoie l'élément associé à la clé
            # depuis le dictionnaire cache_data
            return self.cache_data[key]

        # Renvoie None si la clé n'est pas dans le dictionnaire cache_data
        return None
