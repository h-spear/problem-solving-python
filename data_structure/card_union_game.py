# https://www.acmicpc.net/problem/15903

import heapq

n, m = map(int, input().split())
a = list(map(int, input().split()))
heapq.heapify(a)

for i in range(m):
    one = heapq.heappop(a)
    two = heapq.heappop(a)
    add = one + two
    heapq.heappush(a, add)
    heapq.heappush(a, add)

print(sum(a))
