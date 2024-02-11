# https://www.acmicpc.net/problem/4195

import sys

input = lambda: sys.stdin.readline().rstrip()

for tc in range(int(input())):

    def find(parent, x):
        if parent[x] != x:
            parent[x] = find(parent, parent[x])
        return parent[x]

    def union(parent, a, b):
        a = find(parent, a)
        b = find(parent, b)
        if a < b:
            parent[b] = a
            net[a] += net[b]
            net[b] = 0
        elif a > b:
            parent[a] = b
            net[b] += net[a]
            net[a] = 0

    parent = [0] * 200005
    net = [1] * 200005
    Dict = dict()

    for i in range(1, 200005):
        parent[i] = i

    f = int(input())
    for _ in range(f):
        f1, f2 = input().split()

        if f1 not in Dict.keys():
            Dict[f1] = len(Dict) + 1
        if f2 not in Dict.keys():
            Dict[f2] = len(Dict) + 1

        union(parent, Dict[f1], Dict[f2])
        print(net[find(parent, Dict[f1])])
