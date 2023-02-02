#!/usr/bin/env python3
"""LRUCache module"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """LRUCache class"""

    def __init__(self):
        """ init function """
        super().__init__()
        self.cache_order = []

    def put(self, key, item):
        """ put function """
        if key in self.cache_order:
            self.cache_order.remove(key)
        if len(self.cache_data) == BaseCaching.MAX_ITEMS:
            least_recently_used_key = self.cache_order.pop()
            del self.cache_data[least_recently_used_key]
            print("DISCARD: {}".format(least_recently_used_key))
        if key and item:
            self.cache_order.insert(0, key)
            self.cache_data[key] = item

    def get(self, key):
        """ get function """
        if key and key in self.cache_data:
            self.cache_order.remove(key)
            self.cache_order.insert(0, key)
            return self.cache_data[key]
        return None
