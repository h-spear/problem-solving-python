# https://school.programmers.co.kr/learn/courses/30/lessons/120889


def solution(sides):
    sides.sort()
    if sides[0] + sides[1] > sides[2]:
        return 1
    return 2
