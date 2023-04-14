# https://school.programmers.co.kr/learn/courses/30/lessons/181187

import math


def solution(r1, r2):
    res = 0
    for x in range(1, r2):
        y1 = (r2 ** 2 - x ** 2) ** 0.5
        y2 = max((r1 ** 2 - x ** 2), 0) ** 0.5
        res += math.floor(y1) - math.ceil(y2) + 1

    return (res + 1) * 4
