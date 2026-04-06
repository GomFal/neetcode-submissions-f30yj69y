class Solution:
    def trap(self, height: List[int]) -> int:
        l,r = 0, len(height)-1
        maxLeft, maxRight = height[l], height[r]
        trappedRain = 0

        while l < r:
            if maxLeft < maxRight:
                l += 1
                maxLeft = max(maxLeft, height[l])
                rain = maxLeft - height[l]
                trappedRain += rain
                
            else:
                r -= 1
                maxRight = max(maxRight, height[r])
                rain = maxRight - height[r]
                trappedRain += rain
                
        
        return trappedRain
        