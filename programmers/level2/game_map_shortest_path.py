# https://programmers.co.kr/learn/courses/30/lessons/1844
+
from collections import deque


def solution(maps):
    n, m = len(maps), len(maps[0])
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    q = deque([(0, 0)])
    visited = [[0] * m for _ in range(n)]
    visited[0][0] = 1
    while q:
        x, y = q.popleft()

        if x == n - 1 and y == m - 1:
            return visited[x][y]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if visited[nx][ny]:
                continue
            if maps[nx][ny] == 0:
                continue
            q.append((nx, ny))
            visited[nx][ny] = visited[x][y] + 1

    return -1
