class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not key in self.store:
            self.store[key] = []
        self.store[key].append((timestamp, value)) 

    def get(self, key: str, timestamp: int) -> str:
        if self.store.get(key, 0) == 0:
            return ""

        else:
            search = self.store[key]
            l, r = 0, len(search)-1
            min_key = float("infinity")
            while l <= r:
                m = (l+r)//2
                if search[m][0] == timestamp:
                    return search[m][1]
                elif search[m][0] < timestamp:
                    l = m + 1
                    min_key = m
                else:
                    r = m - 1
            return search[min_key][1] if min_key != float("infinity") else ""
            



