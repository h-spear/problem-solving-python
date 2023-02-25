# https://www.acmicpc.net/problem/24445

from collections import deque


def bfs(start):
    c = 1
    q = deque([start])
    visited[start] = 1

    while q:
        x = q.popleft()

        for next in graph[x]:
            if visited[next]:
                continue
            c += 1
            visited[next] = c
            q.append(next)


n, m, r = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, n + 1):
    graph[i].sort(reverse=True)

bfs(r)

for i in range(1, n + 1):
    print(visited[i])
