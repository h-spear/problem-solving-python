# https://school.programmers.co.kr/learn/courses/15009/lessons/121688

import heapq


def solution(ability, number):
    heapq.heapify(ability)
    for _ in range(number):
        one = heapq.heappop(ability)
        two = heapq.heappop(ability)
        heapq.heappush(ability, one + two)
        heapq.heappush(ability, one + two)

    return sum(ability)
