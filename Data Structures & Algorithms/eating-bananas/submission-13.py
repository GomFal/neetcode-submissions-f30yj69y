class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        min_hours=float("infinity")
        min_rate = max(piles)
        while l <= r:
            rate = (l+r)//2
            time = 0
            for pile in piles:
                time += math.ceil(pile/rate)
            
            if time <= h:
                min_rate = min(rate, min_rate)
                r = rate - 1
            else:
                l = rate + 1
        return min_rate

            

            




