# https://www.acmicpc.net/problem/9095

dp = [0] * 11
dp[1],dp[2],dp[3] = 1,2,4
for i in range(4,11):
  dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

for tc in range(int(input())):
  n = int(input())
  print(dp[n])