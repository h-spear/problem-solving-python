# https://www.acmicpc.net/problem/21278

from collections import deque

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

bfss = [[]]


def bfs(x):
    q = deque([x])
    visited = [-1] * (n + 1)
    visited[x] = 0
    while q:
        now = q.popleft()

        for next in graph[now]:
            if visited[next] != -1:
                continue

            visited[next] = visited[now] + 1
            q.append(next)
    return visited


for i in range(1, n + 1):
    bfss.append(bfs(i))

total = 100000
c1, c2 = 0, 0
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            continue

        sum = 0
        for i in range(1, n + 1):
            sum += min(bfss[a][i], bfss[b][i]) * 2

        if total > sum:
            total = sum
            c1, c2 = a, b

print(c1, c2, total)
