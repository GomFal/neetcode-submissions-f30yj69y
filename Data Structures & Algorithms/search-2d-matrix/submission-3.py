class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        top_row, bottom_row = 0, rows-1
        while top_row <= bottom_row:
            m_row = (top_row+bottom_row)//2
            if matrix[m_row][0] > target:
                bottom_row = m_row - 1
            elif matrix[m_row][-1] < target:
                top_row = m_row + 1
            else:
                break
        row = m_row
        if not top_row <= bottom_row:
            return False
        l, r = 0, cols-1
        while l <= r:
            m = (l+r)//2
            if matrix[row][m] > target:
                r = m - 1
            elif matrix[row][m] < target:
                l = m + 1
            else:
                return True
        return False
        
        