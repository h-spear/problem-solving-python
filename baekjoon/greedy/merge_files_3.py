# https://www.acmicpc.net/problem/13975

import sys
import heapq

input = lambda: sys.stdin.readline().rstrip()

t = int(input())

for test_case in range(t):
    k = int(input())
    page = list(map(int, input().split()))

    heapq.heapify(page)

    answer = 0
    while len(page) > 1:
        first = heapq.heappop(page)
        second = heapq.heappop(page)
        answer += first + second
        heapq.heappush(page, first + second)

    print(answer)
