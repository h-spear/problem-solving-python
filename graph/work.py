# https://www.acmicpc.net/problem/2056

import sys
from collections import defaultdict, deque

input = lambda: sys.stdin.readline().rstrip()
graph = defaultdict(list)
n = int(input())
time = [0] * (n + 1)
in_degree = [0] * (n + 1)

for i in range(1, n + 1):
    input_data = list(map(int, input().split()))
    t, _, *li = input_data
    time[i] = t
    in_degree[i] += len(li)
    for x in li:
        graph[x].append(i)


def topology_sort():
    result = [0] * (n + 1)
    q = deque()
    for i in range(1, n + 1):
        if in_degree[i] == 0:
            q.append(i)
        result[i] = time[i]

    while q:
        x = q.popleft()
        for y in graph[x]:
            in_degree[y] -= 1
            result[y] = max(result[y], result[x] + time[y])
            if in_degree[y] == 0:
                q.append(y)
    print(max(result))


topology_sort()
