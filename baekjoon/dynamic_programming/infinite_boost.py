# https://www.acmicpc.net/problem/17391

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dp = [[500] * m for _ in range(n)]

dp[0][0] = 0
for i in range(n):
    for j in range(m):
        boost = graph[i][j]
        for b in range(1, boost + 1):
            if i + b >= n:
                break
            dp[i + b][j] = min(dp[i + b][j], dp[i][j] + 1)

        for b in range(1, boost + 1):
            if j + b >= m:
                break
            dp[i][j + b] = min(dp[i][j + b], dp[i][j] + 1)


print(dp[n - 1][m - 1])
