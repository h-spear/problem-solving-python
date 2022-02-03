# https://programmers.co.kr/learn/courses/30/lessons/12931


def solution(n):
    return sum(map(int, list(str(n))))
    # return sum(list(map(int, list(str(n)))))
