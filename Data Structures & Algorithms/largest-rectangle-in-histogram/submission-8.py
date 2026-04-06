class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # Pair values (start : height) The start can be moved back when rectangles are popped
        maxArea = 0
        for i, height in enumerate(heights):
            start = i
            while stack and height < stack[-1][1]:
                element = stack.pop()
                maxArea = max(maxArea, (i-element[0])*element[1])
                start = element[0]
            stack.append((start, height))
        print(stack)
        for i, h in stack:
            maxArea = max(maxArea, (len(heights) - i)*h)
        
        return maxArea
        

            
