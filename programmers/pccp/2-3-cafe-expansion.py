# https://school.programmers.co.kr/learn/courses/15009/lessons/121689

from collections import deque


def solution(menu, order, k):
    q = deque()
    orders = deque()
    curr = 0
    answer = 0
    for i, o in enumerate(order):
        orders.append((k * i, o))

    while orders:
        while orders and orders[0][0] <= curr:
            o = orders.popleft()[1]
            q.append(menu[o])

        if curr % k == 0:
            answer = max(answer, len(q))
        else:
            answer = max(answer, len(q) + 1)

        if q:
            curr += q.popleft()
        else:
            curr += 1

    return answer
