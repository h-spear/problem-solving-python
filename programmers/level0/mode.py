# https://school.programmers.co.kr/learn/courses/30/lessons/120812
from collections import Counter


def solution(array):
    counter = Counter(array).most_common(2)
    if not counter:
        return -1
    elif len(counter) == 2:
        if counter[0][1] == counter[1][1]:
            return -1
        else:
            return counter[0][0]
    else:
        return counter[0][0]
