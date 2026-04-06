class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        print(self.cache)

    def get(self, key: int) -> int:
        print(key, self.cache)
        if key in self.cache:
            value = self.cache[key]
            self.cache.pop(key)
            self.cache[key] = value

        return self.cache.get(key, -1)

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.pop(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            lru = next(iter(self.cache))
            del self.cache[lru]
            


        
