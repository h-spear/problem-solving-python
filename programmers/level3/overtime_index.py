# https://school.programmers.co.kr/learn/courses/30/lessons/12927

import heapq


def solution(n, works):
    max_heap = []
    for work in works:
        heapq.heappush(max_heap, (-work, work))

    for _ in range(n):
        if not max_heap:
            return 0

        _, x = heapq.heappop(max_heap)
        x -= 1
        if x == 0:
            continue
        heapq.heappush(max_heap, (-x, x))

    answer = 0
    for _, x in max_heap:
        answer += x ** 2
    return answer
