# https://www.acmicpc.net/problem/4963

from collections import deque

dx = [1, -1, 0, 0, 1, -1, -1, 1]
dy = [0, 0, 1, -1, 1, -1, 1, -1]

while True:
    w, h = map(int, input().split())

    if w == h == 0:
        break

    graph = []

    for _ in range(h):
        input_data = list(map(int, input().split()))
        graph.append(input_data)

    visited = []

    def bfs(x, y):
        if graph[x][y] != 1 or (x, y) in visited:
            return 0

        q = deque([(x, y)])
        while q:
            x, y = q.popleft()

            for i in range(8):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx >= 0 and nx < h and ny >= 0 and ny < w:
                    if graph[nx][ny] == 1 and (nx, ny) not in visited:
                        q.append((nx, ny))
                        visited.append((nx, ny))
        return 1

    result = 0
    for i in range(h):
        for j in range(w):
            result += bfs(i, j)

    print(result)
