# https://school.programmers.co.kr/learn/courses/30/lessons/176963

from collections import defaultdict


def solution(name, yearning, photo):
    d_dict = defaultdict(int)
    d_dict.setdefault(0)
    for n, y in zip(name, yearning):
        d_dict[n] = y

    answer = []
    for p in photo:
        res = 0
        for elem in p:
            res += d_dict[elem]
        answer.append(res)

    return answer
