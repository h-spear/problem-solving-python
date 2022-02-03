# https://programmers.co.kr/learn/courses/30/lessons/68644

from itertools import combinations


def solution(numbers):
    return sorted(list(set(x + y for x, y in combinations(numbers, 2))))
