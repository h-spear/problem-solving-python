# https://www.acmicpc.net/problem/1167

import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

v = int(input())
graph = [[] for _ in range(v + 1)]
for _ in range(v):
    i, *child, _ = map(int, input().split())
    for j in range(0, len(child), 2):
        graph[i].append((child[j], child[j + 1]))


def bfs(start):
    visited = [-1] * (v + 1)
    q = deque()
    q.append(start)
    visited[start] = 0
    farthest_dist = 0
    farthest_node = 0

    while q:
        x = q.popleft()
        for next, dist in graph[x]:
            if visited[next] != -1:
                continue
            visited[next] = visited[x] + dist
            q.append(next)
            if farthest_dist < visited[next]:
                farthest_dist = visited[next]
                farthest_node = next

    return farthest_dist, farthest_node


_, node = bfs(1)
dist, node = bfs(node)
print(dist)
