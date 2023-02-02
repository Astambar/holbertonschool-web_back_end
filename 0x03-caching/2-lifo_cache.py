#!/usr/bin/env python3

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    def __init__(self):
        super().__init__()
        self.cache_data = {}
        self.keys = []

    def put(self, key, item):
        """
        Assign to the dictionary self.cache_data
        the item value for the key key.
        If key or item is None,
        this method should not do anything.
        If the number of items in self.cache_data
        is higher that BaseCaching.MAX_ITEMS,
        discard the last item put in cache (LIFO algorithm)
        and print a message.
        """
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            discarded_key = self.keys.pop()
            self.cache_data.pop(discarded_key)
            print("DISCARD: {}".format(discarded_key))

        self.cache_data[key] = item
        self.keys.append(key)

    def get(self, key):
        """
        Return the value in self.cache_data linked to key.
        If key is None or if the key doesn’t exist
        in self.cache_data, return None.
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
