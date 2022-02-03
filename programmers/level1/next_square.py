# https://programmers.co.kr/learn/courses/30/lessons/12934

import math


def solution(n):
    x = math.sqrt(n)
    # x = n ** (1/2)
    return (x + 1) ** 2 if x == int(x) else -1
