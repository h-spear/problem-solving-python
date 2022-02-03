# https://programmers.co.kr/learn/courses/30/lessons/12903


def solution(s):
    return s[len(s) // 2] if len(s) & 1 else s[len(s) // 2 - 1 : len(s) // 2 + 1]
