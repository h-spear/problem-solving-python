# https://www.acmicpc.net/problem/1202

import heapq

n, k = map(int, input().split())
jewelry = []
bag = []
for _ in range(n):
    m, v = map(int, input().split())
    heapq.heappush(jewelry, (m, v))
for _ in range(k):
    bag.append(int(input()))

answer = 0
bag.sort()
temp = []
for w in bag:
    while jewelry and jewelry[0][0] <= w:
        heapq.heappush(temp, -jewelry[0][-1])
        heapq.heappop(jewelry)

    if temp:
        answer -= heapq.heappop(temp)
    elif not jewelry:
        break

print(answer)
