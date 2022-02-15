# https://www.acmicpc.net/problem/20010
# 트리의 지름까지 구하는 문제(bfs)

import sys
from collections import defaultdict, deque

input = lambda: sys.stdin.readline().rstrip()
n, k = map(int, input().split())
edges = []
parent = [i for i in range(n)]
mst = defaultdict(list)
visited = [0] * n
longest = 0
for _ in range(k):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))


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


def kruskal():
    result = 0
    edges.sort()
    for c, a, b in edges:
        if find(parent, a) == find(parent, b):
            continue
        result += c
        union(parent, a, b)
        mst[a].append((b, c))
        mst[b].append((a, c))
    print(result)


def bfs(x):
    q = deque([x])
    visited = [-1] * n
    visited[x] = 0
    expensive_cost = 0
    expensive_node = 0
    while q:
        x = q.popleft()

        for next, cost in mst[x]:
            if visited[next] != -1:
                continue
            visited[next] = visited[x] + cost
            q.append(next)

            if expensive_cost < visited[next]:
                expensive_cost = visited[next]
                expensive_node = next

    return expensive_cost, expensive_node


def solve():
    kruskal()
    _, node = bfs(1)
    cost, _ = bfs(node)
    print(cost)


solve()
