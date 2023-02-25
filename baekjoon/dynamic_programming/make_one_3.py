# https://www.acmicpc.net/problem/12852

n = int(input())
dp = [int(1e6)] * (n + 1)
path = [0] * (n + 1)

dp[1] = 0
path[1] = -1
for i in range(1, n + 1):
    if i * 3 <= n:
        if dp[i * 3] > dp[i] + 1:
            dp[i * 3] = dp[i] + 1
            path[i * 3] = i
    if i * 2 <= n:
        if dp[i * 2] > dp[i] + 1:
            dp[i * 2] = dp[i] + 1
            path[i * 2] = i
    if i + 1 <= n:
        if dp[i + 1] > dp[i] + 1:
            dp[i + 1] = dp[i] + 1
            path[i + 1] = i

print(dp[n])

r = n
while r != -1:
    print(r, end=" ")
    r = path[r]
