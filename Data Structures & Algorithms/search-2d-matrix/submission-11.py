class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        toprow, botrow = 0, len(matrix)-1
        while toprow <= botrow:
            mrow = (toprow+botrow)//2
            if matrix[mrow][0] <= target <= matrix[mrow][-1]:
                break
            elif matrix[mrow][-1] < target:
                toprow = mrow+1
            else:
                botrow = mrow-1
        
        l, r = 0, len(matrix[mrow])-1
        while l <= r:
            m = (l+r)//2
            if matrix[mrow][m] == target:
                return True
            elif matrix[mrow][m] < target:
                l = m+1
            else:
                r = m-1
        return False
                




        
