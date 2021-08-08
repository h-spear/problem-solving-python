# https://programmers.co.kr/learn/courses/30/lessons/42891

import heapq


def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    heap = []
    for i in range(len(food_times)):
        heapq.heappush(heap, (food_times[i], i + 1))

    remain_food = len(food_times)
    previous_eating = 0
    while (heap[0][0] - previous_eating) * remain_food < k:
        eat = heapq.heappop(heap)[0]
        previous_eating = eat
        k -= eat * remain_food
        remain_food -= 1
    heap.sort(key=lambda x: x[1])
    return heap[k % remain_food][1]


food_times = [3, 1, 2]
k = 5
print(solution(food_times, k))
