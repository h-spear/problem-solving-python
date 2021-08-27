import sys, heapq

input = sys.stdin.readline

n = int(input().rstrip())

heap = []
for _ in range(n):
    x = int(input().rstrip())
    if x == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap)[1])
    else:
        heapq.heappush(heap, (abs(x), x))
