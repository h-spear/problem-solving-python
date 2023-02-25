# https://www.acmicpc.net/problem/11725

import sys

# 반복 제한을 늘려야 통과
sys.setrecursionlimit(10 ** 9)


def dfs(x):
    for i in graph[x]:
        if parent[i] == 0:
            parent[i] = x
            dfs(i)


n = int(input())
graph = [[] for _ in range(n + 1)]
parent = [0] * (n + 1)

for _ in range(n - 1):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

parent[1] = 1
dfs(1)
for x in parent[2:]:
    print(x)
