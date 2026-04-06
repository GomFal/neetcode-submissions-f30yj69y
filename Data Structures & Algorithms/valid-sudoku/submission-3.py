class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        columns = defaultdict(set)
        grids = defaultdict(set)

        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    continue
                elif (board[row][col] not in rows[row] and
                    board[row][col] not in columns[col] and
                    board[row][col] not in grids[(row//3, col//3)]):
                        rows[row].add(board[row][col])
                        columns[col].add(board[row][col])
                        grids[(row//3, col//3)].add(board[row][col])
                else:
                    return False    

        return True
