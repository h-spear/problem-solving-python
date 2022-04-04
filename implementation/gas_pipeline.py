# https://www.acmicpc.net/problem/2931

from collections import deque

r, c = map(int, input().split())
graph = []
for _ in range(r):
    graph.append(list(input()))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
pipeline = {
    "|": [0, 1],
    "-": [2, 3],
    "+": [0, 1, 2, 3],
    "1": [0, 2],
    "2": [1, 2],
    "3": [1, 3],
    "4": [0, 3],
}


def bfs(x, y, d, visited):
    q = deque([(x, y)])

    while q:
        x, y = q.popleft()
        block = graph[x][y]
        if block not in pipeline:
            continue
        for i in pipeline[block]:
            nx = x + dx[i]
            ny = y + dy[i]
            j = 1 - i if i <= 1 else 5 - i

            if nx < 0 or ny < 0 or nx >= r or ny >= c:
                continue
            if visited[nx][ny][j]:
                continue

            visited[nx][ny][j] = 1
            q.append((nx, ny))


def simulation():
    visited = [[[0] * 4 for _ in range(c)] for _ in range(r)]
    for i in range(r):
        for j in range(c):
            for k in range(4):
                bfs(i, j, k, visited)

    for i in range(r):
        for j in range(c):
            if graph[i][j] != ".":
                continue
            if sum(visited[i][j]) == 0:
                continue

            for key, value in pipeline.items():
                temp = [0] * 4
                for x in value:
                    temp[x] = 1
                if temp == visited[i][j]:
                    print(i + 1, j + 1, key)
                    return


simulation()
