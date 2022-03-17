# https://www.acmicpc.net/problem/2410

import math

p = 1000000000
n = int(input())
dp = [[0] * (int(math.log2(n)) + 1) for _ in range(n + 1)]
dp[1][0] = 1

for i in range(2, n + 1):
    if math.log2(i) == int(math.log2(i)):
        dp[i][int(math.log2(i))] += 1

    j = 0
    while 2 ** j <= i:
        dp[i][j] += sum(dp[i - 2 ** j][: j + 1])
        dp[i][j] %= p
        j += 1

print(sum(dp[n]) % p)
