# https://www.acmicpc.net/problem/2217

import sys
n = int(input())

data = []

for _ in range(n):
  data.append(int(sys.stdin.readline().rstrip()))

data.sort()

answer=0 
for rope in data:
  answer= max(answer, rope * n)
  n-=1

print(answer)