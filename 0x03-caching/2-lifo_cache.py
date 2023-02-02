#!/usr/bin/python3
""" 2-lifo_cache.py """
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOCache """

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """ put function """
        if key and item:
            if key in self.cache_data:
                del self.cache_data[key]
            if len(self.cache_data) == self.MAX_ITEMS:
                oldest_key = next(iter(self.cache_data))
                self.cache_data.pop(oldest_key)
                print("DISCARD: {}".format(oldest_key))
            self.cache_data[key] = item

    def get(self, key):
        """ get function """
        return self.cache_data.get(key)
