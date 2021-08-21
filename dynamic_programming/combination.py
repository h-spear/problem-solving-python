# https://www.acmicpc.net/problem/2407

# 조합 combination
# n+1Cr+1 = nCr + nCr+1
# nC0 = nCn = 1

target_n, target_m = map(int, input().split())

dp = [[0] * 101 for _ in range(101)]
for n in range(target_n + 1):
    for m in range(target_m + 1):
        if n == m or m == 0:
            dp[n][m] = 1
        else:
            dp[n][m] = dp[n - 1][m - 1] + dp[n - 1][m]

print(dp[target_n][target_m])
