# https://programmers.co.kr/learn/courses/30/lessons/92342
# 중복조합을 사용하여 전수조사를 하는 방법

from itertools import combinations_with_replacement


def solution(n, info):
    answer = [-1]
    _max = 0

    for case in combinations_with_replacement(range(11), n):
        info_ryan = [0] * 11
        for i in case:
            info_ryan[10 - i] += 1

        score_ryan = 0
        score_apeach = 0

        for i in range(11):
            if info_ryan[i] == 0 and info[i] == 0:
                continue
            elif info_ryan[i] > info[i]:
                score_ryan += 10 - i
            elif info_ryan[i] <= info[i]:
                score_apeach += 10 - i

        if score_ryan <= score_apeach:
            continue

        if _max < score_ryan - score_apeach:
            _max = score_ryan - score_apeach
            answer = info_ryan

    return answer
