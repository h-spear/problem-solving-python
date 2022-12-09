# https://school.programmers.co.kr/learn/courses/30/lessons/142085

import heapq


def solution(n, k, enemy):
    m = len(enemy)
    psum = []

    for v in enemy:
        psum.append((psum[-1] if psum else 0) + v)

    heap = []
    largest = 0
    i = 0
    while i < m:
        curr = enemy[i]
        if len(heap) < k:
            heapq.heappush(heap, curr)
            largest += curr
        elif heap[0] < curr:
            r = heapq.heappop(heap)
            largest -= r
            heapq.heappush(heap, curr)
            largest += curr

        if psum[i] - largest <= n:
            i += 1
        else:
            break

    return i
