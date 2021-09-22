# https://www.acmicpc.net/problem/1325
# pypy3

import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)


def bfs(x):
    visited = [0] * (n + 1)
    visited[x] = 1
    q = deque([x])
    while q:
        now = q.popleft()

        for x in graph[now]:
            if visited[x] == 0:
                visited[x] = 1
                q.append(x)
    return visited.count(1)


rank = []
for i in range(1, n + 1):
    rank.append((i, bfs(i)))

rank.sort(key=lambda x: x[1], reverse=True)

for x, cnt in rank:
    if cnt == rank[0][1]:
        print(x, end=" ")
