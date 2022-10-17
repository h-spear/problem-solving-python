# https://school.programmers.co.kr/learn/courses/30/lessons/120875

from itertools import combinations

INF = float("inf")


def solution(dots):
    for x, y in combinations(range(4), 2):
        a, b = dots[x], dots[y]
        if b[0] != a[0]:
            dec1 = (b[1] - a[1]) / (b[0] - a[0])
        else:
            dec1 = INF

        o = []
        for i in range(4):
            if i != x and i != y:
                o.append(i)

        c, d = dots[o[0]], dots[o[1]]
        if d[0] != c[0]:
            dec2 = (d[1] - c[1]) / (d[0] - c[0])
        else:
            dec2 = INF

        if dec1 == dec2:
            return 1

    return 0
