# https://school.programmers.co.kr/learn/courses/30/lessons/12979

import math


def solution(n, stations, w):
    width = 2 * w + 1

    count = 0
    prev = 1

    for station in stations:
        left = station - w
        right = station + w

        count += math.ceil((left - prev) / width)
        prev = right + 1
    count += math.ceil((n - prev + 1) / width)

    return count
