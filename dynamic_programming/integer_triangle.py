# https://www.acmicpc.net/problem/1932

n = int(input())
triangle = []
dp = [[0] * i for i in range(1, 500 + 1)]
for _ in range(n):
    triangle.append(list(map(int, input().split())))

dp[0][0] = triangle[0][0]
for i in range(1, n):
    for j in range(i + 1):
        if j <= 0:
            prev_left = 0
        else:
            prev_left = dp[i - 1][j - 1]

        if j >= i:
            prev_right = 0
        else:
            prev_right = dp[i - 1][j]

        dp[i][j] = triangle[i][j] + max(prev_right, prev_left)

result = 0
for i in range(n):
    result = max(result, dp[n - 1][i])
print(result)
