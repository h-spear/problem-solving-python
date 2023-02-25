# https://www.acmicpc.net/problem/6064

import sys

input = sys.stdin.readline


for tc in range(int(input().rstrip())):
    m, n, x, y = map(int, input().rstrip().split())

    find = False
    while y <= m * n:
        if x % m == y % m:
            print(y)
            find = True
            break
        y += n
    if find == False:
        print(-1)
