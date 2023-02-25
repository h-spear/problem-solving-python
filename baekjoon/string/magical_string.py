# https://www.acmicpc.net/problem/1097

import sys
from itertools import permutations


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
    ls = len(string)
    lp = len(pattern)
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


input = lambda: sys.stdin.readline().rstrip()
n = int(input())
words = []
for _ in range(n):
    words.append(input())
k = int(input())

answer = 0
for candidate in permutations(words):
    pattern = "".join(candidate)
    string = pattern * 2
    if KMP(string[:-1], pattern) == k:
        answer += 1

print(answer)
