# https://www.acmicpc.net/problem/11048

n, m = map(int, input().split())
graph = []
dp = [[0] * m for _ in range(n)]

for _ in range(n):
    graph.append(list(map(int, input().split())))

dp[0][0] = graph[0][0]
for j in range(1, m):
    dp[0][j] = graph[0][j] + dp[0][j - 1]

for i in range(1, n):
    dp[i][0] = graph[i][0] + dp[i - 1][0]

for i in range(1, n):
    for j in range(1, m):
        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + graph[i][j]


print(dp[n - 1][m - 1])
