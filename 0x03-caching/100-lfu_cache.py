#!/usr/bin/env python3
class LFUCache(BaseCaching):
    def __init__(self):
        super().__init__()
        self.frequency = {}

    def put(self, key, item):
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            min_frequency = min(self.frequency.values())
            keys_with_min_frequency = [key for key, value in self.frequency.items() if value == min_frequency]
            oldest_key = min(keys_with_min_frequency, key=lambda x: self.cache_data[x][1])
            print("DISCARD: {}".format(oldest_key))
            self.cache_data.pop(oldest_key)
            self.frequency.pop(oldest_key)

        self.cache_data[key] = (item, time.time())
        self.frequency[key] = self.frequency.get(key, 0) + 1

    def get(self, key):
        if key is None or key not in self.cache_data:
            return None

        self.frequency[key] += 1
        value, _ = self.cache_data[key]
        return value
