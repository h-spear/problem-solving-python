# https://school.programmers.co.kr/learn/courses/30/lessons/120869

from collections import Counter


def solution(spell, dic):
    counter = Counter(spell)

    for d in dic:
        if counter == Counter(d):
            return 1
    return 2
