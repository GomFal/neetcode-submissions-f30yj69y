class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft, maxRight = height[0], height[len(height)-1]
        l,r = 0, len(height)-1
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
                
        print(l,r)
        return trappedRain
        