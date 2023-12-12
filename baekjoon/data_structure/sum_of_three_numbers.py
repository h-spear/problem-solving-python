# https://www.acmicpc.net/problem/2295

import sys

input = lambda: sys.stdin.readline().rstrip()

N = int(input())
U = [int(input()) for _ in range(N)]

tSet = set()

for x in range(N):
    for y in range(N):
        tSet.add(U[x] + U[y])


answer = 0
for z in range(N):
    for k in range(N):
        if U[k] <= answer:
            continue
        if (U[k] - U[z]) in tSet:
            answer = max(answer, U[k])

print(answer)
