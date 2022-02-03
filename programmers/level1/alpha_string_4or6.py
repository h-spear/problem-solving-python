# https://programmers.co.kr/learn/courses/30/lessons/12918


def solution(s):
    return s.isnumeric() and len(s) == (4 or 6)
    # return s.isdigit() and len(s) in (4, 6)
