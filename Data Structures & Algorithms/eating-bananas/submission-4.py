class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_pile = max(piles)
        l, r = 1, max_pile
        min_k = max_pile

        while l <= r:
            m = (l+r)//2
            k = m
            hours = 0
            for pile in piles:
                hours += math.ceil(pile/k)
                print(pile, k, hours, h)
            print(hours < h)
            if hours <= h:
                print("min_k:", min_k, "k:", k)
                min_k = min(min_k, k)
                r = m - 1
            elif hours > h:
                l = m + 1
            
        return min_k
                
