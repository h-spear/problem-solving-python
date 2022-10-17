# https://school.programmers.co.kr/learn/courses/30/lessons/120860


def solution(dots):
    x1, y1, x2, y2 = 256, 256, -256, -256
    for x, y in dots:
        x1 = min(x1, x)
        x2 = max(x2, x)
        y1 = min(y1, y)
        y2 = max(y2, y)

    return (y2 - y1) * (x2 - x1)
