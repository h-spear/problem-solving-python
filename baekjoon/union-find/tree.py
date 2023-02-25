# https://www.acmicpc.net/problem/4803

from collections import deque


def bfs(graph, node, visited):
    q = deque([node])
    visited[node] = 1
    group = [node]
    while q:
        now = q.popleft()

        for next in graph[now]:
            if visited[next]:
                continue

            group.append(next)
            q.append(next)
            visited[next] = 1
    return group


def grouping(graph, n):
    groups = []
    visited = [0] * (n + 1)
    for node in range(1, n + 1):
        if visited[node]:
            continue
        group = bfs(graph, node, visited)
        groups.append(group)

    return groups


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


def is_cycle(graph, group):
    parent = [i for i in range(len(graph) + 1)]
    edges = set()
    for node in group:
        for next in graph[node]:
            a, b = min(node, next), max(node, next)
            edges.add((a, b))

    for a, b in edges:
        if find(parent, a) == find(parent, b):
            return True
        union(parent, a, b)
    return False


tc = 0
while 1:
    tc += 1
    n, m = map(int, input().split())
    if n == m == 0:
        break

    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    groups = grouping(graph, n)
    cnt = 0
    for group in groups:
        if is_cycle(graph, group):
            pass
        else:
            cnt += 1

    print("Case {}:".format(tc), end=" ")
    if cnt == 0:
        print("No trees.")
    elif cnt == 1:
        print("There is one tree.")
    else:
        print("A forest of {} trees.".format(cnt))
