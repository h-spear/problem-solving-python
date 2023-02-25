# https://www.acmicpc.net/problem/1094

import heapq

x = int(input())
heap = [64]

summation = sum(heap)
while summation != x:
    now = heapq.heappop(heap)

    heapq.heappush(heap, now // 2)
    if summation - now // 2 < x:
        heapq.heappush(heap, now // 2)

    summation = sum(heap)

print(len(heap))
