# https://programmers.co.kr/learn/courses/30/lessons/42578
# 코딩테스트 고득점 Kit : hash

from collections import defaultdict


def solution(clothes):
    hash = defaultdict(int)
    for _, _type in clothes:
        hash[_type] += 1

    answer = 1
    for val in hash.values():
        answer *= val + 1
    return answer - 1
