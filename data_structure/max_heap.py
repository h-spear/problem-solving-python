# https://www.acmicpc.net/problem/11279

import sys, heapq

input = sys.stdin.readline

heap = []
n = int(input().rstrip())

for _ in range(n):
    x = int(input().rstrip())
    if x == 0:
        if len(heap):
            print(heapq.heappop(heap)[1])
        else:
            print(0)
    else:
        heapq.heappush(heap, (-x, x))
