# https://www.acmicpc.net/problem/1715

import heapq

n = int(input())
heap = []
for _ in range(n):
    heapq.heappush(heap, int(input()))

answer = 0

while len(heap) != 1:
    one = heapq.heappop(heap)
    two = heapq.heappop(heap)
    cards = one + two
    answer += cards
    heapq.heappush(heap, cards)

print(answer)
