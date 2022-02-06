# https://programmers.co.kr/learn/courses/30/lessons/42628
# https://www.acmicpc.net/problem/7662
# 코딩테스트 고득점 Kit : Heap

import heapq
from collections import defaultdict


def push(q, item):
    heapq.heappush(q[1], (-item, item))
    heapq.heappush(q[-1], item)
    q["manage"][item] += 1
    q["count"] += 1


def pop(q, sel):
    if q["count"] == 0:
        return

    while 1:
        item = heapq.heappop(q[sel])
        if sel == 1:
            item = item[1]

        if q["manage"][item] == 0:
            continue

        q["manage"][item] -= 1
        if q["manage"][item] == 0:
            del q["manage"][item]
        q["count"] -= 1
        return item


def solution(operations):
    q = {1: [], -1: [], "manage": defaultdict(int), "count": 0}
    for op in operations:
        cmd, operand = op.split()
        if cmd == "I":
            push(q, int(operand))
        elif cmd == "D":
            pop(q, int(operand))

    return [max(q["manage"]), min(q["manage"])] if q["count"] else [0, 0]
