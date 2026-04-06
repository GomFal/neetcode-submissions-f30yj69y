class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        
        maxL = height[l]
        maxR = height[r]
        water = 0

        while l < r:
            if maxL < maxR:
                l += 1 
                if height[l] > maxL:
                    maxL = height[l]
                water += (maxL - height[l])
                print(water, "l: ", l)
                
            else:
                r -= 1 
                if height[r] > maxR:
                    maxR = height[r]
                water += (maxR - height[r])
                print(water, "r: ", r)
                
        return water
            
        