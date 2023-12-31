# https://www.acmicpc.net/problem/1967

from collections import defaultdict, deque
import sys

input = lambda: sys.stdin.readline().rstrip()

n = int(input())
graph = defaultdict(list)
for _ in range(n - 1):
    x, y, w = map(int, input().split())
    graph[x].append((y, w))
    graph[y].append((x, w))


def bfs(x):
    q = deque([x])
    visited = [0] * (n + 1)
    visited[x] = 1
    farthest_node = 0
    farthest_dist = 0
    while q:
        x = q.popleft()

        for next, dist in graph[x]:
            if visited[next]:
                continue
            visited[next] = visited[x] + dist
            q.append(next)

            if farthest_dist < visited[next]:
                farthest_dist = visited[next]
                farthest_node = next
    return max(farthest_dist - 1, 0), farthest_node


_, node = bfs(1)
dist, _ = bfs(node)
print(dist)
