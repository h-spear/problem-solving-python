# https://www.acmicpc.net/problem/2302

n = int(input())
m = int(input())
forbidden = set()
for _ in range(m):
    forbidden.add(int(input()))

# L, R, Center
dp = [[0] * (n + 1) for _ in range(3)]


if 1 not in forbidden:
    dp[1][1] = 1
dp[2][1] = 1

for i in range(2, n + 1):
    dp[2][i] = dp[0][i - 1] + dp[2][i - 1]
    if i in forbidden:
        continue

    if (i - 1) not in forbidden:
        dp[0][i] = dp[1][i - 1]

    if (i + 1) <= n and (i + 1) not in forbidden:
        dp[1][i] = dp[0][i - 1] + dp[2][i - 1]

print(dp[0][n] + dp[1][n] + dp[2][n])
