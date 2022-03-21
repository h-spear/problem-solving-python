# https://www.acmicpc.net/problem/1660

from bisect import bisect_right

INF = float("inf")
n = int(input())
p = 130

triangle = [0] * p
tetrahedron = [0] * p
dp = [INF] * 300001
dp[0] = 0
dp[1] = 1

# make info
for i in range(1, p):
    triangle[i] = triangle[i - 1] + i
    tetrahedron[i] = tetrahedron[i - 1] + triangle[i]

for i in range(2, n + 1):
    idx = bisect_right(tetrahedron, i) - 1
    for j in range(1, idx + 1):
        dp[i] = min(dp[i - tetrahedron[j]] + 1, dp[i])

print(dp[n])
