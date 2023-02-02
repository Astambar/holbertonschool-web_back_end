#!/usr/bin/python3
""" 2-lifo_cache.py """
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOCache """

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """ put function """
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

    def get(self, key):
        """ get function """
        return self.cache_data.get(key, None)
