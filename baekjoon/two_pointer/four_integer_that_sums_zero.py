# https://www.acmicpc.net/problem/7453

import sys

input = lambda: sys.stdin.readline().rstrip()
n = int(input())
A = []
B = []
C = []
D = []

for _ in range(n):
    a, b, c, d = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

S1 = {}
S2 = []

for i in range(n):
    for j in range(n):
        S1[A[i] + B[j]] = S1.get(A[i] + B[j], 0) + 1
        S2.append(C[i] + D[j])

answer = 0
for target in S2:
    answer += S1.get(-target, 0)
print(answer)
