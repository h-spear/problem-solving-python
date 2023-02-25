# https://www.acmicpc.net/problem/1715

import heapq

n = int(input())
heap = []
for _ in range(n):
    heapq.heappush(heap, int(input()))

cards = heapq.heappop(heap)
answer = 0

while heap:
    cards += heapq.heappop(heap)
    answer += cards
    heapq.heappush(heap, cards)
    cards = heapq.heappop(heap)

print(answer)
