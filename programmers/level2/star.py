# https://programmers.co.kr/learn/courses/30/lessons/87377


def solution(line):
    star = set()
    # int(1e6)을 사용하였더니 시간초과가 발생했음
    INF = float("inf")
    bottom, left, top, right = INF, INF, -INF, -INF
    l = len(line)
    for i in range(l):
        for j in range(i, l):
            if i == j:
                continue
            a, b, e = line[i]
            c, d, f = line[j]

            deno = a * d - b * c
            if deno == 0:
                continue
            x = (b * f - e * d) / (deno)
            y = (e * c - a * f) / (deno)

            if x != int(x) or y != int(y):
                continue
            x, y = int(x), int(y)
            star.add((x, y))
            bottom, left = min(y, bottom), min(x, left)
            top, right = max(y, top), max(x, right)

    m, n = top - bottom + 1, right - left + 1
    arr = [["."] * n for _ in range(m)]
    for x, y in star:
        arr[top - y][x - left] = "*"

    return ["".join(r) for r in arr]
