# https://www.acmicpc.net/problem/12865
# 0-1knapsack : DP
# Fraction Knapsack : Greedy

n, k = map(int, input().split())
W = [0]
V = [0]
dp = [[0] * (k + 1) for _ in range(n + 1)]
for _ in range(n):
    w, v = map(int, input().split())
    W.append(w)
    V.append(v)

for i in range(1, n + 1):
    for j in range(1, k + 1):
        if W[i] <= j:
            dp[i][j] = max(dp[i - 1][j], V[i] + dp[i - 1][j - W[i]])
        else:
            dp[i][j] = dp[i - 1][j]

print(dp[n][k])
