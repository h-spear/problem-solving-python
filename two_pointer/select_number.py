# https://www.acmicpc.net/problem/2230

import sys

input = lambda: sys.stdin.readline().rstrip()
n, m = map(int, input().split())
A = []
for _ in range(n):
    A.append(int(input()))

A.sort()

i = 0
j = 1
answer = 2000001234

while i < n and j < n:
    diff = A[j] - A[i]
    if diff == m:
        print(m)
        exit(0)
    elif diff < m:
        j += 1
    else:
        i += 1
        answer = min(answer, diff)

print(answer)
