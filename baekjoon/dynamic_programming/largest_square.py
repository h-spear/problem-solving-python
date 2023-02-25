# https://www.acmicpc.net/problem/1915

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, list(input()))))

dp = [[0] * m for _ in range(n)]
answer = 0

for i in range(n):
    if graph[i][0]:
        dp[i][0] = 1
        answer = 1

for j in range(m):
    if graph[0][j]:
        dp[0][j] = 1
        answer = 1

for i in range(1, n):
    for j in range(1, m):
        if graph[i][j] == 0:
            continue
        val = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1])

        if not val:
            dp[i][j] = 1
        else:
            dp[i][j] = int(val ** 0.5 + 1) ** 2

        answer = max(answer, dp[i][j])

print(answer)
