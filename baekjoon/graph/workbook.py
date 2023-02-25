# https://www.acmicpc.net/problem/1766

import sys
from collections import defaultdict
import heapq


def topology_sort():
    result = []
    q = []
    for i in range(1, n + 1):
        if in_degree[i] == 0:
            heapq.heappush(q, i)

    while q:
        x = heapq.heappop(q)
        result.append(x)
        for v in graph[x]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                heapq.heappush(q, v)

    for node in result:
        print(node, end=" ")


input = lambda: sys.stdin.readline().rstrip()
n, m = map(int, input().split())
graph = defaultdict(list)
in_degree = [0] * (n + 1)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    in_degree[b] += 1

topology_sort()
