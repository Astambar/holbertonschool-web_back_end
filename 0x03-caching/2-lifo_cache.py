class LIFOCache(BaseCaching):
    def __init__(self):
        super().__init__()
    
    def put(self, key, item):
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            last_key = list(self.cache_data.keys())[-1]
            print("DISCARD:", last_key)
            self.cache_data.pop(last_key)
        
        self.cache_data[key] = item

    def get(self, key):
        if key is None or key not in self.cache_data:
            return None
        
        return self.cache_data[key]
