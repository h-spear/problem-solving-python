# https://www.acmicpc.net/problem/1012

from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for tc in range(int(input())):

    m, n, k = map(int, input().split())

    graph = [[0] * m for _ in range(n)]

    for _ in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1

    visited = []
    result = 0

    def bfs(b, a):
        if graph[b][a] == 0 or (b, a) in visited:
            return None

        q = deque([(b, a)])
        visited.append((b, a))

        while q:
            y, x = q.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx >= 0 and nx < m and ny >= 0 and ny < n:
                    if graph[ny][nx] == 1 and (ny, nx) not in visited:
                        q.append((ny, nx))
                        visited.append((ny, nx))

        return True

    for i in range(n):
        for j in range(m):
            if bfs(i, j):
                result += 1

    print(result)
