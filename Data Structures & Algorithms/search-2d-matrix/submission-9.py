class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        toprow, botrow = 0, len(matrix)-1
        while toprow <= botrow:
            mrow = (toprow+botrow)//2
            if matrix[mrow][0] <= target <= matrix[mrow][-1]:
                break
            elif target < matrix[mrow][0]:
                botrow = mrow - 1
            else:
                toprow = mrow + 1
        
        row = matrix[mrow]
        l, r = 0, len(row)-1
        
        while l <= r:
            m = (l+r)//2
            print(m, l, r)
            if row[m] == target:
                return True
            elif row[m] < target:
                l = m + 1
            else:
                r = m - 1

        return False
