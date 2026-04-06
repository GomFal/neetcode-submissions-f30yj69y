class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # (Index of start, Height)
        max_area = 0
        for i, height in enumerate(heights):
            index = i 
            while stack and height < stack[-1][1]:
                max_area = max(max_area, stack[-1][1]*(i-stack[-1][0]))
                index = stack[-1][0]
                stack.pop()
            stack.append((index, height))
    
        for i, h in stack:
            max_area = max(max_area, (len(heights)-i)*h)
        
        return max_area
                


            
