# https://programmers.co.kr/learn/courses/30/lessons/87389


def solution(n):
    for x in range(2, n):
        if (n - 1) % x == 0:
            return x
