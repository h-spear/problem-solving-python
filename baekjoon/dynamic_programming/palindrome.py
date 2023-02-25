# https://www.acmicpc.net/problem/10942

import sys

input = lambda: sys.stdin.readline().rstrip()
n = int(input())
a = list(map(int, input().split()))
m = int(input())
dp = [[0] * n for _ in range(n)]

for l in range(n):
    for s in range(n - l):
        e = s + l
        if s == e:
            dp[s][e] = 1
        elif a[s] == a[e]:
            if s + 1 == e:
                dp[s][e] = 1
            elif dp[s + 1][e - 1] == 1:
                dp[s][e] = 1


for _ in range(m):
    s, e = map(int, input().split())
    print(dp[s - 1][e - 1])
