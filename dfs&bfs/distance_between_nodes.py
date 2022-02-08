# https://www.acmicpc.net/problem/1240

import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()


def bfs(x, target):
    q = deque([x])
    visited = [0] * (n + 1)
    visited[x] = 1
    while q:
        x = q.popleft()

        if x == target:
            return visited[x] - 1

        for next, dist in graph[x]:
            if visited[next]:
                continue
            visited[next] = visited[x] + dist
            q.append(next)


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b, d = map(int, input().split())
    graph[a].append((b, d))
    graph[b].append((a, d))

for _ in range(m):
    a, b = map(int, input().split())
    print(bfs(a, b))
