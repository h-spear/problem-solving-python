# https://www.acmicpc.net/problem/1253

import sys
from bisect import bisect_left, bisect_right

input = lambda: sys.stdin.readline().rstrip()
n = int(input())
A = list(map(int, input().split()))
A.sort()

answer = 0
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        target = A[i] - A[j]
        count = bisect_right(A, target) - bisect_left(A, target)
        if A[j] == target:
            count -= 1
        if A[i] == target:
            count -= 1

        if count >= 1:
            answer += 1
            break

print(answer)
