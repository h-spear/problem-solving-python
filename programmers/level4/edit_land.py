# https://school.programmers.co.kr/learn/courses/30/lessons/12984
# 현재 블록에 존재하는 층만 탐색하면 됨
# -> 2차원 배열을 1차원으로 만들어 계산하는 시간을 줄여야 함.

from bisect import bisect_right, bisect_left


def solution(land, P, Q):
    n = len(land)
    line = []
    psum = []
    candidate = set()

    for i in range(n):
        for j in range(n):
            line.append(land[i][j])
            candidate.add(land[i][j])

    line.sort()
    psum.append(line[0])
    for i in range(1, n * n):
        psum.append(psum[-1] + line[i])
    psum.append(0)
    all_sum = psum[-2]
    len_line = len(line)

    answer = int(1e16)
    for h in candidate:
        lo = bisect_left(line, h)
        hi = bisect_right(line, h)
        added = h * lo - psum[lo - 1]
        deleted = all_sum - psum[hi - 1] - (len_line - hi) * h
        cost = added * P + Q * deleted
        answer = min(answer, cost)

    return answer
