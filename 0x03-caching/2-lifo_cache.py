#!/usr/bin/python3
""" 2-lifo_cache.py """
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOCache """

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """ put function """
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            discarded_key = list(self.cache_data.keys())[0]
            self.cache_data.pop(discarded_key)
            print("DISCARD: {}".format(discarded_key))
        self.cache_data[key] = item

    def get(self, key):
        """ get function """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
