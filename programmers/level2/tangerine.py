# https://school.programmers.co.kr/learn/courses/30/lessons/138476

from collections import Counter


def solution(k, tangerine):
    answer = 0
    for x in sorted(Counter(tangerine).values(), reverse=True):
        if k > 0:
            k -= x
            answer += 1
        else:
            break

    return answer
