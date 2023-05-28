#!/usr/bin/env python3
""" 100-lfu_cache.py """
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ LFUCache """

    def __init__(self):
        super().__init__()
        self.usage = []
        self.frequency = {}

    def put(self, key, item):
        """ put function """
        if key is None or item is None:
            return

        length = len(self.cache_data)
        if length >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
            lfu = min(self.frequency.values())
            lfu_keys = [cache_key for cache_key, frequency in self.frequency.items() if frequency == lfu]
            if len(lfu_keys) > 1:
                lru_lfu = {cache_key: self.usage.index(cache_key) for cache_key in lfu_keys}
                discard = min(lru_lfu.values())
                discard = self.usage[discard]
            else:
                discard = lfu_keys[0]

            print("DISCARD: {}".format(discard))
            del self.cache_data[discard]
            del self.usage[self.usage.index(discard)]
            del self.frequency[discard]

        self.frequency[key] = self.frequency.get(key, 0) + 1
        if key in self.usage:
            del self.usage[self.usage.index(key)]
        self.usage.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """ get function """
        if key is not None and key in self.cache_data.keys():
            del self.usage[self.usage.index(key)]
            self.usage.append(key)
            self.frequency[key] += 1
            return self.cache_data[key]
        return None
