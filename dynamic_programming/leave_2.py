# https://www.acmicpc.net/problem/15486

import sys

input = lambda: sys.stdin.readline().rstrip()

T = [0]
P = [0]
dp = [0] * 1500051

n = int(input())
for _ in range(n):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)

for i in range(1, n + 1):
    dp[i] = max(dp[i], dp[i - 1])
    dp[i + T[i]] = max(dp[i] + P[i], dp[i + T[i]])

print(max(dp[n + 1], dp[n]))
