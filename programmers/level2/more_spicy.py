# https://programmers.co.kr/learn/courses/30/lessons/42626
# 코딩테스트 고득점 Kit : Heap

import heapq


def solution(scoville, K):
    heap = []
    for x in scoville:
        heapq.heappush(heap, x)
    answer = 0
    while heap[0] < K:
        if len(heap) == 1:
            return -1
        one = heapq.heappop(heap)
        two = heapq.heappop(heap)
        heapq.heappush(heap, one + two * 2)
        answer += 1

    return answer
