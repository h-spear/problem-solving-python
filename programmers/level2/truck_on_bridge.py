# https://programmers.co.kr/learn/courses/30/lessons/42583

from collections import deque


def solution(bridge_length, weight, truck_weights):
    bridge = deque([0] * bridge_length)
    truck_weights.reverse()
    on_weight = 0
    answer = 0
    while truck_weights or on_weight != 0:
        removed = bridge.popleft()
        answer += 1
        if removed != 0:
            on_weight -= removed

        if truck_weights and on_weight + truck_weights[-1] <= weight:
            curr = truck_weights.pop()
            bridge.append(curr)
            on_weight += curr
        else:
            bridge.append(0)

    return answer
