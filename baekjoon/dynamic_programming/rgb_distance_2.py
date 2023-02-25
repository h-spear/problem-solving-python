# https://www.acmicpc.net/problem/17404

n = int(input())
cost = []
for _ in range(n):
    cost.append(list(map(int, input().split())))

INF = float("inf")
answer = INF

for k in range(3):
    dp = [[INF] * 3 for _ in range(n)]
    dp[0][k] = cost[0][k]
    dp[1] = [cost[0][k] + cost[1][0], cost[0][k] + cost[1][1], cost[0][k] + cost[1][2]]
    dp[1][k] = INF
    for i in range(2, n):
        dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + cost[i][0]
        dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + cost[i][1]
        dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + cost[i][2]

    dp[n - 1][k] = INF
    answer = min(answer, min(dp[n - 1]))


print(answer)
