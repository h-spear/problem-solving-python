# https://www.acmicpc.net/problem/11723

import sys

input = sys.stdin.readline

m = int(input())
S = set()
for _ in range(m):
    cmd = input().rstrip().split()
    if len(cmd) >= 2:
        item = int(cmd[1])

    if cmd[0] == "add":
        if item not in S:
            S.add(item)
    if cmd[0] == "check":
        print(1 if item in S else 0)
    if cmd[0] == "remove":
        if item in S:
            S.remove(item)
    if cmd[0] == "toggle":
        if item in S:
            S.remove(item)
        else:
            S.add(item)
    if cmd[0] == "all":
        S = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
    if cmd[0] == "empty":
        S.clear()
