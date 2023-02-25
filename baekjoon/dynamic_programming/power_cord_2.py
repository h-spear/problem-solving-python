# https://www.acmicpc.net/problem/2568
# LIS

import sys, heapq
from bisect import bisect_left

input = lambda: sys.stdin.readline().rstrip()
n = int(input())
heap = []
answer = set()
for _ in range(n):
    a, b = map(int, input().split())
    heapq.heappush(heap, (a, b))
    answer.add(a)

A = []
while heap:
    item = heapq.heappop(heap)
    A.append((item[1], item[0]))

q = []
temp = []
for i, x in enumerate(A):
    if not q or q[-1] < x:
        q.append(x)
        temp.append((len(q) - 1, x[1]))
    else:
        idx = bisect_left(q, x)
        q[idx] = x
        temp.append((idx, x[1]))


now = len(q) - 1
for i in range(len(temp) - 1, -1, -1):
    if temp[i][0] == now:
        answer.remove(temp[i][1])
        now -= 1

print(len(answer))
for x in sorted(list(answer)):
    print(x)
