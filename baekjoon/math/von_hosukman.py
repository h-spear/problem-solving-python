# https://www.acmicpc.net/problem/21275

import sys

_dict = dict()
for i in range(10):
    _dict[str(i)] = i
for i in range(26):
    _dict[chr(97 + i)] = i + 10


def to_base10(num: str, base: int) -> int:
    decimal = 0
    for i, x in enumerate(num):
        decimal += _dict[x] * base ** (len(num) - i - 1)
    return decimal


def max_base(nums: str):
    return _dict[max(nums)] + 1


def find_XAB(num1: str, num2: str) -> None:
    answer = None
    for A in range(max_base(num1), 37):
        for B in range(max_base(num2), 37):
            if A == B:
                continue
            dec_A = to_base10(num1, A)
            dec_B = to_base10(num2, B)
            if dec_A != dec_B:
                continue
            if dec_A >= sys.maxsize:
                continue
            if dec_B >= sys.maxsize:
                continue
            if answer != None:
                print("Multiple")
                return
            answer = (dec_A, A, B)

    if answer == None:
        print("Impossible")
        return

    for x in answer:
        print(x, end=" ")


nums = input().split()
find_XAB(nums[0], nums[1])
