# https://www.acmicpc.net/problem/9465

import sys

input = sys.stdin.readline

for tc in range(int(input())):
    graph = []
    dp = [[0] * 100002 for _ in range(2)]
    n = int(input().rstrip())

    for _ in range(2):
        input_data = list(map(int, input().rstrip().split()))
        input_data.insert(0, 0)
        graph.append(input_data)

    for i in range(1, n + 1):
        dp[0][i] = graph[0][i] + max(dp[1][i - 1], dp[0][i - 2], dp[1][i - 2])
        dp[1][i] = graph[1][i] + max(dp[0][i - 1], dp[0][i - 2], dp[1][i - 2])

    print(max(dp[0][n], dp[1][n]))
