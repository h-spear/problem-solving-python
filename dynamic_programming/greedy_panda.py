# https://www.acmicpc.net/problem/1937

import sys

input = lambda: sys.stdin.readline().rstrip()
n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dp = [[-1] * n for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
answer = -1


def dfs(x, y):
    global answer
    if dp[x][y] != -1:
        return dp[x][y]

    dp[x][y] = 0
    candidate = []
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            continue
        if graph[nx][ny] <= graph[x][y]:
            continue
        candidate.append(1 + dfs(nx, ny))

    if not candidate:
        dp[x][y] = 1
    else:
        dp[x][y] = max(candidate)

    answer = max(answer, dp[x][y])

    return dp[x][y]


for i in range(n):
    for j in range(n):
        dfs(i, j)

print(answer)
