# https://school.programmers.co.kr/learn/courses/30/lessons/152996

from collections import defaultdict


def solution(weights):
    counter = defaultdict(int)
    for weight in weights:
        counter[weight] += 1

    answer = 0
    for _, val in counter.items():
        answer += val * (val - 1) // 2

    for w in counter:
        for cand in [w * 4 / 3, w * 3 / 2, w * 2]:
            if cand != int(cand):
                continue
            if cand in counter:
                answer += counter[w] * counter[cand]

    return answer
