class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        max_price = 0
        while r < len(prices):
            max_price = max(prices[r]-prices[l], max_price)
            if prices[l] > prices[r]:
                l = r    
            r += 1
        return max_price
            



