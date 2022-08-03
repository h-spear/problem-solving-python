# https://www.acmicpc.net/problem/2616

n = int(input())
a = list(map(int, input().split()))
m = int(input())
dp = [[0] * (n + 1) for _ in range(4)]

psum = [0] * (n + 1)
for i in range(1, n + 1):
    psum[i] = psum[i - 1] + a[i - 1]

for i in range(1, 4):
    for j in range(m, n + 1):
        dp[i][j] = max(dp[i][j - 1], dp[i - 1][j - m] + psum[j] - psum[j - m])

for x in dp:
    print(x)
print(dp[3][n])
