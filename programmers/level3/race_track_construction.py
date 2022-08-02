# https://school.programmers.co.kr/learn/courses/30/lessons/67259

from collections import deque


def solution(board):
    n = len(board)
    INF = float("inf")

    # up, donw, left, right
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def bfs(x, y):
        visited = [[[INF] * 2 for _ in range(n)] for _ in range(n)]
        for i in range(2):
            visited[0][0][i] = 0

        q = deque([(x, y, 0, -1)])
        while q:
            x, y, cost, _dir = q.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or ny < 0 or nx >= n or ny >= n:
                    continue
                if board[nx][ny]:
                    continue

                if _dir == -1:
                    pass
                elif (_dir == i // 2) and (cost + 100 >= visited[nx][ny][i // 2]):
                    continue
                elif (_dir != i // 2) and (cost + 600 >= visited[nx][ny][i // 2]):
                    continue

                if _dir == -1 or _dir == i // 2:
                    q.append((nx, ny, cost + 100, i // 2))
                    visited[nx][ny][i // 2] = cost + 100
                elif _dir != i // 2:
                    q.append((nx, ny, cost + 600, i // 2))
                    visited[nx][ny][i // 2] = cost + 600

        return min(visited[n - 1][n - 1])

    return bfs(0, 0)
