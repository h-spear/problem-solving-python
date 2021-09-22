# https://www.acmicpc.net/problem/5567

import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def bfs():
    visited = [-1] * (n + 1)
    q = deque([1])
    visited[1] = 0
    while q:
        now = q.popleft()

        for x in graph[now]:
            if visited[x] == -1:
                visited[x] = visited[now] + 1
                q.append(x)

    cnt = 0
    for x in visited:
        if x == 1 or x == 2:
            cnt += 1

    return cnt


print(bfs())
