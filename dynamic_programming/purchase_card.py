# https://www.acmicpc.net/problem/11052

import sys

input = sys.stdin.readline

n = int(input())
card = list(map(int, input().split()))
dp = [0] * n
dp[0] = card[0]
dp[1] = max(card[0] * 2, card[1])

for i in range(2, n):
    MAX = -1
    for j in range(i):
        MAX = max(dp[j] + dp[i - j - 1], MAX)
    dp[i] = max(MAX, card[i])

print(dp[n - 1])
