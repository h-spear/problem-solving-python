# https://www.acmicpc.net/problem/2579

import sys
input = sys.stdin.readline
n = int(input())

stair = [0]
for _ in range(n):
  stair.append(int(input()))

dp = [0] * (n+1)
dp[1] = stair[1]

if n != 1:
  dp[2] = stair[1] + stair[2]

for i in range(3,n+1):
  dp[i] = stair[i] + max(stair[i-1] + dp[i-3], dp[i-2])
print(dp[n])
