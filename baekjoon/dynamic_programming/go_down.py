# https://www.acmicpc.net/problem/2096
# sliding window

import sys

input = sys.stdin.readline
INF = int(1e9)

n = int(input().rstrip())
max_dp = [[-INF] * 3 for _ in range(3)]
min_dp = [[INF] * 3 for _ in range(3)]

for i in range(1, n + 1):
    data = list(map(int, input().rstrip().split()))
    if n == 1:
        print(max(data), min(data))
        break

    for j in range(3):
        if i == 1:
            max_dp[j][j] = data[j]
        else:
            first = data[0] + max(max_dp[j][0], max_dp[j][1])
            second = data[1] + max(max_dp[j][0], max_dp[j][1], max_dp[j][2])
            third = data[2] + max(max_dp[j][1], max_dp[j][2])
            max_dp[j] = [first, second, third]

    for j in range(3):
        if i == 1:
            min_dp[j][j] = data[j]
        else:
            first = data[0] + min(min_dp[j][0], min_dp[j][1])
            second = data[1] + min(min_dp[j][0], min_dp[j][1], min_dp[j][2])
            third = data[2] + min(min_dp[j][1], min_dp[j][2])
            min_dp[j] = [first, second, third]

if n != 1:
    print(
        max(max(max_dp[0], max_dp[1], max_dp[2])),
        min(min(min_dp[0], min_dp[1], min_dp[2])),
    )
