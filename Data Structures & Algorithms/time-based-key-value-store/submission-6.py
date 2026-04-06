class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        search_timestamp = self.store.get(key, [])
        l, r = 0, len(search_timestamp)-1
        value = ""

        while l <= r:
            m = (l+r)//2 

            if search_timestamp[m][1] <= timestamp:
                value = search_timestamp[m][0]
                l = m + 1

            else:
                r = m - 1
        
        return value


