#!/usr/bin/env python3
""" 100-lfu_cache.py """
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ LFUCache """

    def __init__(self):
        super().__init__()
        self.usage_order = []
        self.key_frequencies = {}

    def put(self, key, item):
        """ put function """
        if key is None or item is None:
            return

        cache_length = len(self.cache_data)
        if cache_length >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
            min_frequency = min(self.key_frequencies.values())
            min_frequency_keys = [cache_key for cache_key, frequency in self.key_frequencies.items() if frequency == min_frequency]
            if len(min_frequency_keys) > 1:
                lru_lfu = {cache_key: self.usage_order.index(cache_key) for cache_key in min_frequency_keys}
                discard_index = min(lru_lfu.values())
                discard_key = self.usage_order[discard_index]
            else:
                discard_key = min_frequency_keys[0]

            print("DISCARD: {}".format(discard_key))
            del self.cache_data[discard_key]
            del self.usage_order[self.usage_order.index(discard_key)]
            del self.key_frequencies[discard_key]

        self.key_frequencies[key] = self.key_frequencies.get(key, 0) + 1
        if key in self.usage_order:
            del self.usage_order[self.usage_order.index(key)]
        self.usage_order.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """ get function """
        if key is not None and key in self.cache_data.keys():
            del self.usage_order[self.usage_order.index(key)]
            self.usage_order.append(key)
            self.key_frequencies[key] += 1
            return self.cache_data[key]
        return None
