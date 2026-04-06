class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r:
            m = (l+r)//2
            k = m
            hours = 0
            for pile in piles:
                hours += math.ceil(float(pile)/k)
                
            if hours <= h:
                min_k = min(res, k)
                r = m - 1
            else:
                l = m + 1
            
        return min_k
                
