class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for r in range(len(board)):
            seen = set()
            for c in range(len(board[0])):
                if board[r][c].isdigit():
                    if board[r][c] in seen:
                        return False

                    else:
                        seen.add(board[r][c])

        for c in range(len(board[0])):
            seen = set()
            for r in range(len(board)):
                if board[r][c].isdigit():
                    if board[r][c] in seen:
                        return False

                    else:
                        seen.add(board[r][c])

        for r in range(0, len(board), 3):
            for c in range(0, len(board[0]), 3):
                seen = set()
                for i in range(r, r + 3):
                    for j in range(c, c + 3):
                        if board[i][j].isdigit():
                            if board[i][j] in seen:
                                return False

                            else:
                                seen.add(board[i][j])

        return True