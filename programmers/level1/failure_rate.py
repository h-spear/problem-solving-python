# https://programmers.co.kr/learn/courses/30/lessons/42889
# sorting

from collections import defaultdict


def solution(N, stages):
    _dict = defaultdict(int)

    for x in stages:
        _dict[x] += 1

    n = len(stages)
    for stage in range(1, N + 1):
        if n == 0:
            _dict[stage] = 0
            continue
        _dict[stage], n = _dict[stage] / n, n - _dict[stage]

    return [
        x[0]
        for x in sorted(_dict.items(), key=lambda x: (x[1], -x[0]), reverse=True)
        if x[0] <= N
    ]
