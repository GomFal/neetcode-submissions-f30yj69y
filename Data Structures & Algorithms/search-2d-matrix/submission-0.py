class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l_c, r_c = 0, len(matrix[0])-1
        l_r, r_r = 0, len(matrix)-1
        while l_r <= r_r:
            m_r = (l_r + r_r)//2
            if matrix[m_r][l_c] <= target <= matrix[m_r][r_c]:
                while l_c <= r_c:
                    m_c = (l_c + r_c)//2
                    if matrix[m_r][m_c] < target:
                        l_c = m_c + 1
                        
                    elif matrix[m_r][m_c] > target:
                        r_c = m_c - 1
                        
                    else:
                        return True
            elif matrix[m_r][l_c] > target:
                r_r = m_r - 1
            else:
                l_r = m_r + 1
        return False
        
        