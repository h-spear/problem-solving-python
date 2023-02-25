# https://www.acmicpc.net/problem/1520
# dfs + dp

m, n = map(int, input().split())
graph = []
dp = [[0] * n for _ in range(m)]
for _ in range(m):
    graph.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[-1] * n for _ in range(m)]


def dfs(x, y):
    if x == m - 1 and y == n - 1:
        return 1
    if visited[x][y] != -1:
        return visited[x][y]

    visited[x][y] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or ny < 0 or nx >= m or ny >= n:
            continue
        if graph[nx][ny] < graph[x][y]:
            visited[x][y] += dfs(nx, ny)

    return visited[x][y]


print(dfs(0, 0))
