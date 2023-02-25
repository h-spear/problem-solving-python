# https://www.acmicpc.net/problem/7579

import sys

input = lambda: sys.stdin.readline().rstrip()
n, m = map(int, input().split())
a = list(map(int, input().split()))
c = list(map(int, input().split()))
dp = [[0] * (sum(c) + 1) for _ in range(n + 1)]

answer = 123456789
for i in range(1, n + 1):
    for j in range(0, sum(c) + 1):
        if j - c[i - 1] >= 0:
            dp[i][j] = max(dp[i - 1][j - c[i - 1]] + a[i - 1], dp[i - 1][j])
        else:
            dp[i][j] = dp[i - 1][j]

        if dp[i][j] >= m:
            answer = min(answer, j)


print(answer)
