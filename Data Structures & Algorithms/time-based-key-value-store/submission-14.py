class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not key in self.store:
            self.store[key] = []
        self.store[key].append((timestamp, value)) 

    def get(self, key: str, timestamp: int) -> str:
        search = self.store.get(key, [])
        l, r = 0, len(search)-1
        res = ""
        while l <= r:
            m = (l+r)//2
            if search[m][0] <= timestamp:
                res = search[m][1]
                l = m + 1   
            else:
                r = m - 1
        return res
            



