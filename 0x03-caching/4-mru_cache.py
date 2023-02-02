#!/usr/bin/python3
""" 4-mru_cache.py """

from collections import OrderedDict

BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """ Most Recently Used Cache Class """

    def __init__(self):
        super().__init__()
        self.recently_used_keys = OrderedDict()

    def put(self, key, item):
        """ Add item to the cache with a specific key """
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

    def get(self, key):
        """ Retrieve item from the cache with a specific key """
        if key in self.cache_data:
            self.recently_used_keys.move_to_end(key, False)
            return self.cache_data[key]

        return None
