class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        rectangles = [] # (Index, Height)
        max_area = 0

        for i, height in enumerate(heights):
            index = i
            while rectangles and rectangles[-1][1] > height:
                index = rectangles[-1][0]
                max_area = max(max_area, rectangles[-1][1]*(i-index))
                rectangles.pop()

            rectangles.append((index, height))
        
        print(rectangles, max_area)
        
        for i, height in rectangles:
            max_area = max(max_area, (len(heights)-i)*height)
        
        return max_area

            
