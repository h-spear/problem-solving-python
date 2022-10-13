# https://school.programmers.co.kr/learn/courses/30/lessons/120886

from collections import Counter


def solution(before, after):
    return 1 if Counter(before) == Counter(after) else 0
