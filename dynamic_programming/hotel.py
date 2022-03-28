# https://www.acmicpc.net/problem/1106

c, n = map(int, input().split())
W = [0]
V = [0]
dp = [0] * 1000000
for _ in range(n):
    w, v = map(int, input().split())
    W.append(w)
    V.append(v)


i = 1
while 1:
    for j in range(1, len(W)):
        if i - W[j] >= 0:
            dp[i] = max(dp[i], dp[i - W[j]] + V[j])
            if dp[i] >= c:
                print(i)
                exit(0)
    i += 1
