# https://programmers.co.kr/learn/courses/30/lessons/12912


def solution(a, b):
    a, b = min(a, b), max(a, b)
    return sum(range(a, b + 1))
