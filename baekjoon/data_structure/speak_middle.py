# https://www.acmicpc.net/problem/1655

import sys, heapq

input = lambda: sys.stdin.readline().rstrip()
left = []
right = []
mid = 0
n = int(input())

for i in range(n):
    number = int(input())
    if i == 0:
        mid = number
        print(mid)
        continue

    if number >= mid:
        heapq.heappush(right, number)
        if len(left) + 1 < len(right):
            heapq.heappush(left, (-mid, mid))
            mid = heapq.heappop(right)
    else:
        heapq.heappush(left, (-number, number))
        if len(right) + 1 <= len(left):
            heapq.heappush(right, mid)
            mid = heapq.heappop(left)[1]
    print(mid)
