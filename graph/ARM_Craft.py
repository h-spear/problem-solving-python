# https://www.acmicpc.net/problem/1005

import sys
from collections import defaultdict, deque

for tc in range(int(input())):

    def topology_sort():
        result = [0] * (n + 1)
        q = deque()
        for i in range(1, n + 1):
            if in_degree[i] == 0:
                q.append(i)
            result[i] = d[i - 1]

        while q:
            x = q.popleft()

            for v in graph[x]:
                in_degree[v] -= 1
                result[v] = max(result[v], result[x] + d[v - 1])
                if in_degree[v] == 0:
                    q.append(v)

        print(result[w])

    input = lambda: sys.stdin.readline().rstrip()

    n, k = map(int, input().split())
    d = list(map(int, input().split()))
    graph = defaultdict(list)
    in_degree = [0] * (n + 1)
    for _ in range(k):
        a, b = map(int, input().split())
        graph[a].append(b)
        in_degree[b] += 1
    w = int(input())

    topology_sort()
