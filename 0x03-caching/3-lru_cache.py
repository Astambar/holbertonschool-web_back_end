#!/usr/bin/env python3
class LRUCache(BaseCaching):
    def __init__(self):
        super().__init__()
        self.cache_data = {}

    def put(self, key, item):
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            lru = min(self.cache_data, key=lambda x: self.cache_data[x][1])
            print("DISCARD:", lru)
            del self.cache_data[lru]

    def get(self, key):
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
