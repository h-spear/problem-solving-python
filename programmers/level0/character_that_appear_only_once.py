# https://school.programmers.co.kr/learn/courses/30/lessons/120896

from collections import Counter


def solution(s):
    counter = Counter(s)
    answer = []
    for k, v in counter.items():
        if v == 1:
            answer.append(k)
    answer.sort()
    return "".join(answer)
