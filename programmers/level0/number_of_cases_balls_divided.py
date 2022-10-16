# https://school.programmers.co.kr/learn/courses/30/lessons/120840


def facto(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res


def solution(balls, share):
    n, m = balls, share
    return facto(n) // ((facto(n - m)) * facto(m))
