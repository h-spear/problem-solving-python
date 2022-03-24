# https://www.acmicpc.net/problem/19947
# profit dict를 0.05, 0.2, 0.35로 설정하여 x + x + profit[j]를 하면 오답
# 바로 1.05, 1.2, 1.35를 곱하는 방식으로 계산해야 함

h, y = map(int, input().split())

dp = [0] * 11
dp[0] = h
profit = {1: 1.05, 3: 1.2, 5: 1.35}
for i in range(0, y + 1):
    for j in [1, 3, 5]:
        if i + j > 10:
            continue
        dp[i + j] = max(dp[i + j], int(dp[i] * profit[j]))

print(dp[y])
