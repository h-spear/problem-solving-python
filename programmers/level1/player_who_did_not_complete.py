# https://programmers.co.kr/learn/courses/30/lessons/42576

from collections import defaultdict, Counter


def solution(participant, completion):
    completion.append("")
    _dict = defaultdict(int)
    for x, y in zip(participant, completion):
        _dict[x] += 1
        _dict[y] -= 1
    return Counter(_dict).most_common(1)[0][0]
