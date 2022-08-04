# https://school.programmers.co.kr/learn/courses/30/lessons/42891

import heapq


def solution(food_times, k):
    heap = []
    for idx, food_time in enumerate(food_times):
        heapq.heappush(heap, (food_time, idx + 1))

    time = 0
    while heap:
        lh = len(heap)
        around_time = lh * (heap[0][0] - time)

        if around_time <= k:
            k -= lh * (heap[0][0] - time)
            time += heap[0][0] - time
            heapq.heappop(heap)
        else:
            break

    foods = []
    while heap:
        _, idx = heapq.heappop(heap)
        foods.append(idx)
    foods.sort()

    if foods:
        return foods[k % len(foods)]
    return -1
