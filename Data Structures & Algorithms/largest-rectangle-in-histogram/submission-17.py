class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # (Index, Height)
        max_area = 0

        for i, h in enumerate(heights):
            index = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                max_area = max((i-index)*height, max_area)
            stack.append((index, h))
        
        # now, we should have only the heights in descending order

        for i, h in stack:
            max_area = max(max_area, (len(heights)-i)*h)
        
        return max_area


                


            
