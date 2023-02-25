# https://www.acmicpc.net/problem/11437
# Tree
# LCA Algorithm

import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 5)


n = int(input())
graph = defaultdict(list)
visited = [0] * (n + 1)
parent = [0] * (n + 1)
depth_info = [0] * (n + 1)
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(x, depth):
    depth_info[x] = depth
    visited[x] = 1
    for y in graph[x]:
        if visited[y]:
            continue
        parent[y] = x
        dfs(y, depth + 1)


dfs(1, 0)

m = int(input())
for _ in range(m):
    p, q = map(int, input().split())

    if depth_info[p] > depth_info[q]:
        p, q = q, p

    while depth_info[p] != depth_info[q]:
        q = parent[q]

    while p != q:
        p = parent[p]
        q = parent[q]

    print(p)
