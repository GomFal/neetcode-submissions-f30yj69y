class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        l = 0
        for r in range(1, len(prices)):
            print("l: ", prices[l], "r: ", prices[r])
            if prices[l] < prices[r]:
                print(maxP)
                maxP = max(maxP, (prices[r] - prices[l]))
            else:
                l = r
        return maxP
            



