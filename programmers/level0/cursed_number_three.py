# https://school.programmers.co.kr/learn/courses/30/lessons/120871


def solution(n):
    i = 0
    c = 0
    while 1:
        i += 1
        if i % 3 == 0:
            continue
        if "3" in str(i):
            continue
        c += 1

        if c == n:
            return i

    return None
