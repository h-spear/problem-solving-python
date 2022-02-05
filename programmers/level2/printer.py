# https://programmers.co.kr/learn/courses/30/lessons/42587
# 코딩테스트 고득점 Kit : Stack/Queue

from collections import deque


def solution(priorities, location):
    q = deque([(x, i) for i, x in enumerate(priorities)])

    cnt = 0
    while q:
        max_prio = max([prio for prio, _ in q])
        prio, idx = q.popleft()
        if prio == max_prio:
            cnt += 1
            if idx == location:
                break
            continue
        q.append((prio, idx))
    return cnt
