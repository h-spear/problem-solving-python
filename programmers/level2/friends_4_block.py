# https://programmers.co.kr/learn/courses/30/lessons/17679


def is_score_block(x, y, board):
    for dx, dy in [(1, 0), (0, 1), (1, 1)]:
        nx = x + dx
        ny = y + dy
        if board[nx][ny] != board[x][y]:
            return False
    return {(x, y), (x + 1, y), (x, y + 1), (x + 1, y + 1)}


def remove_block(m, n, board):
    removed = False
    blocks = set()
    for i in range(m - 1):
        for j in range(n - 1):
            if board[i][j] == "0":
                continue
            result = is_score_block(i, j, board)
            if result == False:
                continue
            removed = True
            blocks.update(result)

    for x, y in blocks:
        board[x][y] = "0"

    for i in range(m - 1, 0, -1):
        for j in range(n):
            if board[i][j] != "0":
                continue

            k = 0
            while i - k >= 0 and board[i - k][j] == "0":
                k += 1

            if i - k < 0:
                continue
            board[i - k][j], board[i][j] = board[i][j], board[i - k][j]

    return removed


def calc_score(m, n, board):
    score = 0
    for i in range(m):
        for j in range(n):
            if board[i][j] != "0":
                continue
            score += 1
    return score


def solution(m, n, board):
    board = [list(row) for row in board]
    while remove_block(m, n, board):
        pass
    return calc_score(m, n, board)
