#!/usr/bin/env python3
"""
Module for FIFOCache
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    Class that implements a FIFO cache
    """

    def __init__(self):
        """
        Initialize the cache
        """
        super().__init__()
        self.cache_data = {}
        self.keys = []

    def put(self, key, item):
        """
        Add an item to the cache
        """
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            discarded_key = self.keys.pop(0)
            self.cache_data.pop(discarded_key)
            print("DISCARD: {}".format(discarded_key))

        self.cache_data[key] = item
        self.keys.append(key)

    def get(self, key):
        """
        Retrieve an item from the cache
        """
        if key is None or key not in self.cache_data:
            return None

        return self.cache_data[key]
