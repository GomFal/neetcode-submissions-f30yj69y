class Solution:
    def maxArea(self, heights: List[int]) -> int:
        most_water = 0
        l, r = 0, len(heights)-1

        while l < r:
            most_water = max(most_water, (r-l)*min(heights[l], heights[r]))

            if heights[l]<heights[r]:
                l += 1
            else:
                r -= 1

        return most_water