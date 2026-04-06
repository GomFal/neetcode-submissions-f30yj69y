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
                print("maxLeft ", maxLeft)
                print("rain added on the left:", rain) if rain > 0 else None
                trappedRain += rain
                

            else:
                r -= 1
                maxRight = max(maxRight, height[r])
                print("maxRight ",maxRight)
                rain = maxRight - height[r]
                
                print("rain added on the right:", rain) if rain > 0 else None
                trappedRain += rain
                
        print(l,r)

        return trappedRain
        