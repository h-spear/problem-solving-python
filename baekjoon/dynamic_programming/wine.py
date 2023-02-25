# https://www.acmicpc.net/problem/2156

import sys

input = sys.stdin.readline

n = int(input())
data = [0]
dp = [0] * (n + 2)
for _ in range(n):
    data.append(int(input()))

dp[1] = data[1]

if n != 1:
    dp[2] = data[1] + data[2]

for i in range(4, n + 1):
    dp[i] = max(
        data[i] + dp[i - 2],
        data[i] + data[i - 1] + dp[i - 3],
        data[i] + data[i - 1] + dp[i - 4],
    )

print(max(dp))
