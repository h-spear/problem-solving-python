# https://www.acmicpc.net/problem/7511

import sys

input = lambda: sys.stdin.readline().rstrip()
answer = []


def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


for tc in range(1, int(input()) + 1):
    n = int(input())
    k = int(input())
    parent = [i for i in range(n + 1)]
    for _ in range(k):
        a, b = map(int, input().split())
        union(parent, a, b)

    m = int(input())
    result = []
    for _ in range(m):
        u, v = map(int, input().split())
        if find(parent, u) == find(parent, v):
            result.append(1)
        else:
            result.append(0)

    answer.append(result)


for i, result in enumerate(answer):
    print("Scenario {}:".format(i + 1))
    for x in result:
        print(x)
    print()
