#!/usr/bin/env python3
"""LRUCache module"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """LRUCache class"""

    def __init__(self):
        """ init function """
        super().__init__()
        self.cache_list = []

    def put(self, key, item):
        """ put function """
        if key in self.cache_list:
            self.cache_list.remove(key)
        if len(self.cache_data) == BaseCaching.MAX_ITEMS:
            LeastRecentlyUsedKey = self.cache_list.pop()
            del self.cache_data[LeastRecentlyUsedKey]
            print("DISCARD: {}".format(LeastRecentlyUsedKey))
        if key and item:
            self.cache_list.insert(0, key)
            self.cache_data[key] = item

    def get(self, key):
        """ get function """
        if key and key in self.cache_data:
            self.cache_list.remove(key)
            self.cache_list.insert(0, key)
            return self.cache_data[key]
        return None
