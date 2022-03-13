# https://programmers.co.kr/learn/courses/30/lessons/12936

import math


def solution(n, k):

    nums = [i for i in range(1, n + 1)]
    answer = []
    for i in range(n, 0, -1):
        facto = math.factorial(i - 1)
        num = nums.pop(int((k - 1) // facto))
        k %= facto
        answer.append(num)

    return answer
