# https://leetcode.com/problems/valid-sudoku/


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def valid_check(x, y):
            num = board[x][y]

            for i in range(9):
                if i == x:
                    continue
                if board[i][y] == num:
                    return False

            for j in range(9):
                if j == y:
                    continue
                if board[x][j] == num:
                    return False

            _x = (x // 3) * 3
            _y = (y // 3) * 3
            for i in range(_x, _x + 3):
                for j in range(_y, _y + 3):
                    if i == x and j == y:
                        continue
                    if board[i][j] == num:
                        return False

            return True

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if not valid_check(i, j):
                    return False
        return True
