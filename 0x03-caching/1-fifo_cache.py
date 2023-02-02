class FIFOCache(BaseCaching):

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            discarded_key = next(iter(self.cache_data))
            self.cache_data.pop(discarded_key)
            print("DISCARD:", discarded_key)

        self.cache_data[key] = item

    def get(self, key):
        if key is None or key not in self.cache_data:
            return None

        return self.cache_data[key]
