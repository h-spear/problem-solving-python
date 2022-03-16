# https://www.acmicpc.net/problem/1535

import sys

input = lambda: sys.stdin.readline().rstrip()

n = int(input())
health = [0]
health.extend(list(map(int, input().split())))
joy = [0]
joy.extend(list(map(int, input().split())))


def knapsack():
    dp = [[0] * 100 for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, 100):
            if health[i] <= j:
                dp[i][j] = max(dp[i - 1][j], joy[i] + dp[i - 1][j - health[i]])
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[n][99]


print(knapsack())
