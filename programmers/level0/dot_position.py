# https://school.programmers.co.kr/learn/courses/30/lessons/120841


def solution(dot):
    x, y = dot
    if x > 0 and y > 0:
        return 1
    elif x < 0 and y > 0:
        return 2
    elif x < 0 and y < 0:
        return 3
    return 4
