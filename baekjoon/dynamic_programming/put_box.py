# https://www.acmicpc.net/problem/1965

n = int(input())
size = [0]
size.extend(list(map(int, input().split())))
dp = [0] * (n + 1)

for i in range(1, n + 1):
    for j in range(i):
        if size[j] < size[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
