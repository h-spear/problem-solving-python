# https://school.programmers.co.kr/learn/courses/30/lessons/120880


def solution(numlist, n):
    return sorted(numlist, key=lambda x: (abs(n - x), -x))
