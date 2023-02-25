# https://www.acmicpc.net/problem/1987
# PyPy3

import sys

r, c = map(int, input().split())

graph = []
for _ in range(r):
    graph.append(list(map(lambda x: ord(x) - 65, sys.stdin.readline().rstrip())))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
visited = [False] * 26

result = 0


def dfs(count, x, y):
    global result
    result = max(result, count)
    visited[graph[x][y]] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < r and ny >= 0 and ny < c:
            if visited[graph[nx][ny]] == False:
                dfs(count + 1, nx, ny)
                visited[graph[nx][ny]] = False


dfs(1, 0, 0)
print(result)
