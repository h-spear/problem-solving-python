# https://school.programmers.co.kr/learn/courses/30/lessons/120866


def solution(board):
    n = len(board)
    checker = [[0] * n for _ in range(n)]
    dx = [1, -1, 0, 0, 1, 1, -1, -1]
    dy = [0, 0, 1, -1, 1, -1, 1, -1]
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0:
                continue
            checker[i][j] = 1
            for k in range(8):
                ni = i + dx[k]
                nj = j + dy[k]
                if ni < 0 or nj < 0 or ni >= n or nj >= n:
                    continue
                checker[ni][nj] = 1

    answer = n * n
    for r in checker:
        answer -= sum(r)
    return answer
