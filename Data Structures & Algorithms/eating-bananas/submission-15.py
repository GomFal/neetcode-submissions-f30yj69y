class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        
        min_rate = max(piles)
        while l <= r:
            rate = (l+r)//2
            time = 0
            for pile in piles:
                time += math.ceil(float(pile)/rate)
            
            if time <= h:
                min_rate = rate
                r = rate - 1
            else:
                l = rate + 1
        return min_rate

            

            




