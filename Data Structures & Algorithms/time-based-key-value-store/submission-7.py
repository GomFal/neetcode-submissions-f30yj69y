class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        
        search = self.store[key]
        l, r = 0, len(search)-1
        res = ""
        while l <= r:
            m = (l+r)//2
            if search[m][1] <= timestamp:
                res = search[m][0]
                l = m + 1
            elif search[m][1] > timestamp:
                r = m - 1
        return res




