# https://programmers.co.kr/learn/courses/30/lessons/42627#
# 코딩테스트 고득점 Kit : Heap

import heapq
from collections import deque


def solution(jobs):
    heap = []
    jobs_q = deque(sorted(jobs))
    time = 0
    working_time = 0
    while 1:
        if not jobs_q and not heap:
            break

        while jobs_q and jobs_q[0][0] <= time:
            arrive_time, remaining_time = jobs_q.popleft()
            heapq.heappush(heap, (remaining_time, arrive_time))

        # 작업들이 아직 도착하지 않은 경우
        if len(heap) == 0:
            time = jobs_q[0][0]
            continue

        remaining_time, arrive_time = heapq.heappop(heap)
        wait_time = time - arrive_time
        time += remaining_time
        working_time += wait_time + remaining_time

    return working_time // len(jobs)
