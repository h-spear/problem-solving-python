# https://programmers.co.kr/learn/courses/30/lessons/12953

import math


def solution(arr):
    answer = 1
    for x in arr:
        answer = (answer * x) // math.gcd(answer, x)
    return answer
