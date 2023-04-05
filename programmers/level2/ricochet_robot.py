# https://school.programmers.co.kr/learn/courses/30/lessons/169199

from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def solution(board):
    n = len(board)
    m = len(board[0])
    visited = [[[[0] * m for k in range(n)] for j in range(m)] for i in range(n)]
    board = [list(line) for line in board]

    x, y = 0, 0
    gx, gy = 0, 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == "R":
                x, y = i, j
                board[i][j] = "."
            elif board[i][j] == "G":
                gx, gy = i, j
                board[i][j] = "."

    q = deque([(x, y, 0)])

    while q:
        x, y, c = q.popleft()

        if x == gx and y == gy:
            return c

        for i in range(4):
            nx, ny = x, y
            while nx >= 0 and ny >= 0 and nx < n and ny < m and board[nx][ny] == ".":
                nx += dx[i]
                ny += dy[i]

            nx -= dx[i]
            ny -= dy[i]

            if visited[x][y][nx][ny]:
                continue
            q.append((nx, ny, c + 1))
            visited[x][y][nx][ny] = 1

    return -1
