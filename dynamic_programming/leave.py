# https://www.acmicpc.net/problem/14501

n = int(input())
t = [0]
p = [0]
dp = [0] * 25
for _ in range(n):
    input_t, input_p = map(int, input().split())
    t.append(input_t)
    p.append(input_p)


for i in range(1, n + 1):
    dp[i + 1] = max(dp[i + 1], dp[i])
    dp[i + t[i]] = max(dp[i + t[i]], dp[i] + p[i])

print(dp[n + 1])
