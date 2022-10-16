# https://school.programmers.co.kr/learn/courses/30/lessons/120815


def solution(n):
    i = 1
    while 1:
        if (6 * i) % n == 0:
            return i
        i += 1
