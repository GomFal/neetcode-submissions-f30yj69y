class Solution:
    def trap(self, height: List[int]) -> int:
        maxL, maxR = height[0], height[-1]
        l, r = 1, len(height)-2
        max_water = 0
        while l <= r:
            if maxL < maxR:
                maxL = max(maxL, height[l])
                max_water += maxL - height[l]
                l += 1
            else:
                maxR = max(maxR, height[r])
                max_water += maxR - height[r]
                r -= 1
        return max_water 


        