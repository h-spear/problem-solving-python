# https://www.acmicpc.net/problem/17626
# pypy3, bad code

import math

n = int(input())
dp = [10000] * 50001

for i in range(1, n + 1):
    proximate = int(math.sqrt(i))
    if proximate ** 2 == i:
        dp[i] = 1
    else:
        for j in range(proximate, 0, -1):
            dp[i] = min(dp[i], 1 + dp[i - j ** 2])


print(dp[n])
