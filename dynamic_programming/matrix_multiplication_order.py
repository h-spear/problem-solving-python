# https://www.acmicpc.net/problem/11049
# https://www.youtube.com/watch?v=u1gIkGXUqBQ
# https://www.youtube.com/watch?v=Tdl6VP4bS90

n = int(input())
matrix = []
for _ in range(n):
    matrix.append(tuple(map(int, input().split())))

dp = [[0] * n for _ in range(n)]

cnt = 0
for i in range(1, n):
    for j in range(n - i):
        x = j + i
        dp[j][x] = 2 ** 32
        for k in range(j, x):
            dp[j][x] = min(
                dp[j][x],
                dp[j][k] + dp[k + 1][x] + matrix[j][0] * matrix[k][1] * matrix[x][1],
            )

print(dp[0][n - 1])
