# https://programmers.co.kr/learn/courses/30/lessons/12980


def solution(n):
    cnt = 0
    while n:
        if n & 1 == 1:
            cnt += 1
        n //= 2
    return cnt
