#!/usr/bin/python3
""" 4-mru_cache.py """

from collections import OrderedDict

BaseCaching = __import__('base_caching').BaseCaching


class MostRecentlyUsedCache(BaseCaching):
    """ MRUCache """

    def __init__(self):
        super().__init__()
        self.most_recently_used = OrderedDict()

    def put(self, key, item):
        """ put function """
        if not key or not item:
            return
        self.cache_data[key] = item
        self.most_recently_used[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            item_discarded = next(iter(self.most_recently_used))
            del self.cache_data[item_discarded]
            print("DISCARD:", item_discarded)
        if len(self.most_recently_used) > BaseCaching.MAX_ITEMS:
            self.most_recently_used.popitem(last=False)
        self.most_recently_used.move_to_end(key, False)

    def get(self, key):
        """ get function """
        if key in self.cache_data:
            self.most_recently_used.move_to_end(key, False)
            return self.cache_data[key]
        return None
