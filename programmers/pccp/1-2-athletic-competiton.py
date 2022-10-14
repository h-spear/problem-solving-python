# https://school.programmers.co.kr/learn/courses/15008/lessons/121684

from itertools import permutations


def solution(ability):
    answer = 0
    m = len(ability)
    n = len(ability[0])
    for candidate in permutations(range(m), n):
        temp = 0
        for c, r in enumerate(candidate):
            temp += ability[r][c]
        answer = max(answer, temp)

    return answer
