# https://programmers.co.kr/learn/courses/30/lessons/12940


def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)


def solution(n, m):
    _gcd = gcd(n, m)
    return [_gcd, n * m // _gcd]
