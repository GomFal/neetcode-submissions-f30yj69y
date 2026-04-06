class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        toprow, botrow = 0, len(matrix)-1
        while toprow <= botrow:
            mrow = (toprow+botrow)//2
            if target >= matrix[mrow][0] and target <= matrix[mrow][-1]:
                break 
            elif target < matrix[mrow][0]:
                botrow = mrow - 1
            elif target > matrix[mrow][-1]:
                toprow = mrow + 1
        
        l, r = 0, len(matrix[mrow])-1
        # Now we search for the item inside the row
        
        while l <= r:
            m = (l+r)//2
            if matrix[mrow][m] > target:
                r = m - 1
            elif matrix[mrow][m] < target:
                l = m + 1
            else:
                return True
        return False
        