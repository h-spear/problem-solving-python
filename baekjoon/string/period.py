# https://www.acmicpc.net/problem/3779

import sys

input = lambda: sys.stdin.readline().rstrip()


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


def testcase(i, table):
    print("Test case #{}".format(i))
    for j in range(len(table)):
        if table[j] == 0:
            continue
        if (j + 1) % (j + 1 - table[j]) != 0:
            continue
        print(j + 1, (j + 1) // (j + 1 - table[j]))
    print()


tc = 0
while 1:
    tc += 1
    n = input()
    if n == "0":
        break
    string = input()
    table = failure(string)
    testcase(tc, table)
