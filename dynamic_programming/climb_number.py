# https://www.acmicpc.net/problem/11057

# dp
n = int(input())
dp = [[0] * 10 for _ in range(n + 1)]
for i in range(10):
    dp[1][i] = 1

for i in range(2, n + 1):
    for j in range(10):
        for k in range(j + 1):
            dp[i][j] += dp[i - 1][k]
        dp[i][j] %= 10007

print(sum(dp[n]) % 10007)


# 중복조합을 이용한 풀이
# math.comb : 조합의 경우의 수를 반환해줌
import math

n = int(input())
print(math.comb(n + 9, n) % 10007)

