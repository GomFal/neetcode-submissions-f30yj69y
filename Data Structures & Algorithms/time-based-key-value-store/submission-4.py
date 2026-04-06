class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if self.store.get(key, 0) == 0:
            self.store[key] = [] 
        self.store[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if self.store.get(key, 0) == 0:
            return ""
        else:
            search_timestamp = self.store[key]

        l, r = 0, len(search_timestamp)-1
        value = ""
        while l <= r:
            m = (l+r)//2 

            if search_timestamp[m][1] < timestamp:
                value = search_timestamp[m][0]
                print(search_timestamp[m][1], timestamp)
                l = m + 1
            elif search_timestamp[m][1] > timestamp:
                r = m - 1
            else:
                value = search_timestamp[m][0]
                l = m + 1
        
        return value


