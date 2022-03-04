# https://www.acmicpc.net/problem/1699

import math


def solution(n):
    dp = [100] * 100001
    dp[0], dp[1], dp[2], dp[3] = 0, 1, 2, 3

    for i in range(4, n + 1):
        sq = int(math.sqrt(i))
        # 무조건 가장 큰 제곱 수를 빼는 것이 정답이 아닐 수 있음
        for j in range(1, sq + 1):
            dp[i] = min(dp[i - j * j] + 1, dp[i])

    return dp[n]


n = int(input())
print(solution(n))
