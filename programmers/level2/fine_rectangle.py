# https://programmers.co.kr/learn/courses/30/lessons/62048


def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)


def solution(w, h):
    return w * h - (w + h - gcd(w, h))
