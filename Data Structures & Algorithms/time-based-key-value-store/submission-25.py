class TimeMap:

    def __init__(self):
        self.timemap = {}


    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timemap:
            self.timemap[key] = []
        self.timemap[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        
        search_list = self.timemap.get(key, [])
        l, r = 0, len(search_list)-1
        
        res = ""
        while l <= r:
            m = (l+r)//2
            
            if search_list[m][0] <= timestamp:
                res = search_list[m][1]
                l = m + 1
            else:
                r = m - 1
        return res


            

        





