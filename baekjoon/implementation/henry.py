# https://www.acmicpc.net/problem/10253
# 입력 자체가 기약분수인 경우 체크해야 함.

import sys, math

input = lambda: sys.stdin.readline().rstrip()


def round(a, b):
    return math.ceil(b / a)


def calc_fraction(a, b, c, d):
    return a * d - b * c, b * d


def simulation(a, b):
    while 1:
        if a == 1:  ########
            print(b)
            return

        x = round(a, b)
        a, b = calc_fraction(a, b, 1, x)

        _gcd = math.gcd(a, b)
        a //= _gcd
        b //= _gcd


for tc in range(int(input())):
    a, b = map(int, input().split())
    simulation(a, b)
