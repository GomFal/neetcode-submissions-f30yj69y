class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((value, timestamp)) 
        
        

    def get(self, key: str, timestamp: int) -> str:
        # Binary Search
        search = self.store.get(key, [])
        recent_value = ""
        if not search:
            return recent_value 
        l, r = 0, len(search)-1
        
        while l <= r:
            m = (l+r)//2
            if search[m][1] <= timestamp:
                recent_value = search[m][0]
                l = m + 1
            else:
                r = m - 1
        return recent_value





