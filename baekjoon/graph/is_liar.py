# https://www.acmicpc.net/problem/14676

from collections import defaultdict
import sys

input = lambda: sys.stdin.readline().rstrip()

n, m, k = map(int, input().split())
graph = defaultdict(list)
info = []
for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)

info = [tuple(map(int, input().split())) for _ in range(k)]
unit = [0] * (n + 1)


def func():
    for cmd, i in info:
        if cmd == 1:
            for x in graph[i]:
                if unit[x] >= 1:
                    continue
                print("Lier!")
                return
            unit[i] += 1
        else:
            if unit[i] == 0:
                print("Lier!")
                return
            unit[i] -= 1
    print("King-God-Emperor")


func()
