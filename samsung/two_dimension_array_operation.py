# https://www.acmicpc.net/problem/17140

import sys
from collections import defaultdict

input = lambda: sys.stdin.readline().rstrip()
l = 100
r, c, k = map(int, input().split())
A = [[0] * l for _ in range(l)]
row, col = 3, 3
for i in range(3):
    input_data = list(map(int, input().split()))
    for j in range(3):
        A[i][j] = input_data[j]


def operation_R():
    global col, A
    max_len = 0
    temp = [[0] * l for _ in range(l)]
    for i in range(row):
        hash = defaultdict(int)
        for j in range(col):
            if A[i][j] != 0:
                hash[A[i][j]] += 1
        j = 0
        lt = 0
        for a, b in sorted(hash.items(), key=lambda x: (x[1], x[0])):
            temp[i][j] = a
            temp[i][j + 1] = b
            j += 2
            lt += 2

            if j == l:
                break
        max_len = max(max_len, lt)

    col = max_len
    A = temp


def operation_C():
    global row, A
    max_len = 0
    temp = [[0] * l for _ in range(l)]
    for j in range(col):
        hash = defaultdict(int)
        for i in range(row):
            if A[i][j] != 0:
                hash[A[i][j]] += 1
        i = 0
        lt = 0
        for a, b in sorted(hash.items(), key=lambda x: (x[1], x[0])):
            temp[i][j] = a
            temp[i + 1][j] = b
            i += 2
            lt += 2

            if i == l:
                break
        max_len = max(max_len, lt)

    row = max_len
    A = temp


def one_second():
    global row, col
    if row >= col:
        operation_R()
    else:
        operation_C()


def simul():
    s = 0
    while s <= 100:
        if A[r - 1][c - 1] == k:
            break

        one_second()
        s += 1

    if s == 101:
        print(-1)
    else:
        print(s)


simul()
