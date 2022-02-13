# https://www.acmicpc.net/problem/14567

import sys
from collections import defaultdict, deque

input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())
in_degree = [0] * (n + 1)
result = [0] * (n + 1)
graph = defaultdict(list)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    in_degree[b] += 1


def topology_sort():
    q = deque()
    for i in range(1, n + 1):
        if in_degree[i] == 0:
            q.append(i)
            result[i] = 1

    while q:
        x = q.popleft()

        for y in graph[x]:
            result[y] = max(result[y], result[x] + 1)
            in_degree[y] -= 1
            if in_degree[y] == 0:
                q.append(y)

    for i in range(1, n + 1):
        print(result[i], end=" ")


topology_sort()
