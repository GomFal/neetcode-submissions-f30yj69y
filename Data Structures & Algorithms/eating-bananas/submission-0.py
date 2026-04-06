class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles) # We create the array of possible values
        res = r                # At least the max value will be a solution
        while l <= r:
            k = (l+r)//2
            hours = 0
            for p in piles:
                hours += math.ceil(p/k)
            if hours <= h:
                res = k
                r = k-1
            else:
                l = k + 1
        
        return res