# https://www.acmicpc.net/problem/2565

n = int(input())
data = []
for _ in range(n):
    data.append(tuple(map(int, input().split())))

data.sort()

dp = [1] * n

for i in range(1, len(data)):
    for j in range(0, i):
        if data[j][1] < data[i][1]:
            dp[i] = max(dp[j] + 1, dp[i])

print(n - max(dp))
