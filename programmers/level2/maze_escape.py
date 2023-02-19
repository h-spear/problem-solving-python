# https://school.programmers.co.kr/learn/courses/30/lessons/159993

from collections import deque

INF = float("inf")
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def solution(maps):
    def bfs(sx, sy, tx, ty):
        q = deque([(sx, sy)])
        visited = [[0] * m for _ in range(n)]
        visited[sx][sy] = 1

        while q:
            x, y = q.popleft()

            if x == tx and y == ty:
                return visited[x][y] - 1

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or ny < 0 or nx >= n or ny >= m:
                    continue
                if visited[nx][ny]:
                    continue
                if maps[nx][ny] == "X":
                    continue
                q.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1

        return INF

    n = len(maps)
    m = len(maps[0])

    entrance_point = None
    lever_point = None
    exit_point = None

    for i in range(n):
        for j in range(m):
            if maps[i][j] == "S":
                entrance_point = (i, j)
            elif maps[i][j] == "L":
                lever_point = (i, j)
            elif maps[i][j] == "E":
                exit_point = (i, j)

    answer = bfs(*entrance_point, *lever_point) + bfs(*lever_point, *exit_point)

    if answer == INF:
        return -1
    return answer
