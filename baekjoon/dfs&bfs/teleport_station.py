# https://www.acmicpc.net/problem/18232

import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())
s, e = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def bfs(x, y):
    visited = [0] * (n + 1)
    visited[x] = 1
    q = deque([x])
    while q:
        x = q.popleft()
        if x == y:
            return visited[x] - 1

        if x + 1 <= n and not visited[x + 1]:
            visited[x + 1] = visited[x] + 1
            q.append(x + 1)

        if x - 1 >= 1 and not visited[x - 1]:
            visited[x - 1] = visited[x] + 1
            q.append(x - 1)

        for next in graph[x]:
            if not visited[next]:
                q.append(next)
                visited[next] = visited[x] + 1


print(bfs(s, e))
