# https://www.acmicpc.net/problem/1495

n, s, m = map(int, input().split())
v = list(map(int, input().split()))
v.insert(0, 0)

dp = [[0] * (m + 1) for _ in range(n + 1)]
dp[0][s] = 1
for i in range(1, n + 1):
    for idx, vol in enumerate(dp[i - 1]):
        if vol:
            if idx + v[i] <= m:
                dp[i][idx + v[i]] = 1

            if idx - v[i] >= 0:
                dp[i][idx - v[i]] = 1

possible = False
for i in range(m, -1, -1):
    if dp[n][i] == 1:
        print(i)
        possible = True
        break
if not possible:
    print(-1)
