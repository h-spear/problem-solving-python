# https://www.acmicpc.net/problem/12764

import heapq

n = int(input())
t = []
for _ in range(n):
    t.append(tuple(map(int, input().split())))
t.sort()

x = 0
heap = []
counter = [0] * n
cp = [i for i in range(n)]

for s, e in t:
    x = max(x, len(heap))

    while heap and heap[0][0] < s:
        _, c = heapq.heappop(heap)
        heapq.heappush(cp, c)

    num = heapq.heappop(cp)
    if not heap:
        heapq.heappush(heap, (e, num))
        counter[num] += 1
    elif heap[0][0] > s:
        heapq.heappush(heap, (e, num))
        counter[num] += 1
        x = max(x, len(heap))


print(x)
print(*counter[:x])
