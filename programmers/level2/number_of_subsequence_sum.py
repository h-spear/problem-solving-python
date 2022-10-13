# https://school.programmers.co.kr/learn/courses/30/lessons/131701

from collections import deque


def solution(elements):
    s = set()
    elements = deque(elements)
    for _ in range(len(elements)):
        temp = 0
        for i in range(len(elements)):
            temp += elements[i]
            s.add(temp)
        elements.append(elements.popleft())

    return len(s)
