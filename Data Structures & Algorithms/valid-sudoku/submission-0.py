class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            rows = set()
            cols = set()
            box = set()
            
            for j in range(9):
                if board[i][j] in rows:
                    return False
                elif board[i][j] != '.':
                    rows.add(board[i][j])

                if board[j][i] in cols:
                    return False
                elif board[j][i] != '.':
                    cols.add(board[j][i])

                if board[3 * (i // 3) + j // 3][3 * (i % 3) + j % 3] in box:
                    return False
                elif board[3 * (i // 3) + j // 3][3 * (i % 3) + j % 3] != '.':
                    box.add(board[3 * (i // 3) + j // 3][3 * (i % 3) + j % 3])

        return True

            