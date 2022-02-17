# https://www.acmicpc.net/problem/11585

import math


def failure(pattern):
    table = [0] * len(pattern)
    j = 0
    for i in range(1, len(pattern)):
        while j > 0 and pattern[i] != pattern[j]:
            j = table[j - 1]

        if pattern[i] == pattern[j]:
            j += 1
            table[i] = j
    return table


def KMP(string, pattern):
    ls, lp = len(string), len(pattern)
    table = failure(pattern)
    j = 0
    cnt = 0
    for i in range(ls):
        while j > 0 and string[i] != pattern[j]:
            j = table[j - 1]

        if string[i] == pattern[j]:
            if j == lp - 1:
                cnt += 1
                j = table[j]
            else:
                j += 1

    return cnt


N = int(input())
pattern = input().replace(" ", "")
text = input().replace(" ", "")
cnt = KMP(text * 2, pattern)
if pattern == text:
    cnt -= 1

_gcd = math.gcd(cnt, N)
print("{0}/{1}".format(cnt // _gcd, N // _gcd))
