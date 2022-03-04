# https://www.acmicpc.net/problem/10164


def fn(n, m):
    dp = [[0] * m for _ in range(n)]

    for i in range(n):
        dp[i][0] = 1
    for j in range(m):
        dp[0][j] = 1

    for i in range(1, n):
        for j in range(1, m):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    return dp[n - 1][m - 1]


n, m, k = map(int, input().split())
if k == 0:
    print(fn(n, m))
else:
    x = (k - 1) // m + 1
    y = k % m
    if y == 0:
        y = m
    to_circle = fn(x, y)
    to_dest = fn(n - x + 1, m - y + 1)
    print(to_circle * to_dest)
