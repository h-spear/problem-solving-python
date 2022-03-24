# https://www.acmicpc.net/problem/9711

import sys

input = lambda: sys.stdin.readline().rstrip()

tc = int(input())
for c in range(1, tc + 1):
    p, q = map(int, input().split())
    dp = [0] * (p + 3)
    dp[0] = 0
    dp[1] = 1
    for i in range(2, p + 1):
        dp[i] = (dp[i - 1] + dp[i - 2]) % q

    print("Case #{}: {}".format(c, dp[p] % q))
