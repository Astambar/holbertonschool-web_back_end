#!/usr/bin/env python3
""" 100-lfu_cache.py """
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    LFU Cache Class

    This class implements a Least Frequently
    Used (LFU) cache. It stores a limited
    number of items, discarding the least frequently
    used items when the cache is full.
    """

    def __init__(self):
        super().__init__()

        # A list to store the usage of each key in the cache
        self.usage = []

        # A dictionary to store the frequency of each key in the cache
        self.frequency = {}

    def put(self, key, item):
        """
        Put function

        Add an item to the cache with the given key.
        If the cache is full, it discards
        the least frequently used item.
        """
        if key is None or item is None:
            return

        # If the cache is full and the given key
        # is not in the cache, find the least
        # frequently used key and discard it.
        MAX_ITEMS = BaseCaching.MAX_ITEMS
        if len(self.cache_data) >= MAX_ITEMS and key not in self.cache_data:
            least_frequent_use = min(self.frequency.values())
            keys_with_least_frequency = []
            for k, v in self.frequency.items():
                if v == least_frequent_use:
                    keys_with_least_frequency.append(k)

            # If there is more than one key with the same least frequency,
            # find the
            # key that was used least recently among them.
            if len(keys_with_least_frequency) > 1:
                least_recently_used = {}
                for k in keys_with_least_frequency:
                    least_recently_used[k] = self.usage.index(k)
                key_to_discard = min(least_recently_used.values())
                key_to_discard = self.usage[key_to_discard]
            else:
                key_to_discard = keys_with_least_frequency[0]

            print("DISCARD: {}".format(key_to_discard))
            del self.cache_data[key_to_discard]
            del self.usage[self.usage.index(key_to_discard)]
            del self.frequency[key_to_discard]

        # Update the frequency of the given key
        if key in self.frequency:
            self.frequency[key] += 1
        else:
            self.frequency[key] = 1

        # Update the usage of the given key
        if key in self.usage:
            del self.usage[self.usage.index(key)]
        self.usage.append(key)

        # Add the item to the cache with the given key
        self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve the item associated with the given key from the cache
        """
        # If the key is not None and it exists in the cache_data dictionary
        if key is not None and key in self.cache_data.keys():
            # Remove the key from its current position in the usage list
            self.usage.remove(key)
            # Add the key to the end of the usage list
            self.usage.append(key)
            # Increment the frequency count for the key
            self.frequency[key] += 1
            # Return the item associated with the key
            # from the cache_data dictionary
            return self.cache_data[key]
        # Return None if the key is not in the cache_data dictionary
        return None
