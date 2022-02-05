# https://programmers.co.kr/learn/courses/30/lessons/42586
# 코딩테스트 고득점 Kit : Stack/Queue

import math
from collections import deque


def solution(progresses, speeds):
    answer = []
    q = deque([math.ceil((100 - p) / s) for p, s in zip(progresses, speeds)])
    day, cnt = q[0], 0
    print(q)
    while q:
        x = q.popleft()
        print(day, x, cnt)
        if day < x:
            day = x
            answer.append(cnt)
            cnt = 1
        else:
            cnt += 1
    answer.append(cnt)
    return answer
