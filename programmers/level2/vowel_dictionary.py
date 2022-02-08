# https://programmers.co.kr/learn/courses/30/lessons/84512

from itertools import product

_dict = []
for l in range(1, 6):
    for word in list(product("AEIOU", repeat=l)):
        _dict.append("".join(word))
_dict.sort()


def solution(word):
    return _dict.index(word) + 1
