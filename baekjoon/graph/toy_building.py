# https://www.acmicpc.net/problem/2637

from collections import defaultdict, deque

n = int(input())
m = int(input())
graph = defaultdict(list)
result = [0] * (n + 1)
in_degree = [0] * (n + 1)
basic_part = [True] * (n + 1)

for _ in range(m):
    x, y, k = map(int, input().split())
    basic_part[x] = False
    graph[x].append((y, k))
    in_degree[y] += 1


def topology_sort():
    result[n] = 1
    q = deque()
    for i in range(1, n + 1):
        if in_degree[i] == 0:
            q.append(i)

    while q:
        x = q.popleft()

        for y, cost in graph[x]:
            result[y] += result[x] * cost
            in_degree[y] -= 1
            if in_degree[y] == 0:
                q.append(y)

    for i in range(1, n + 1):
        if basic_part[i] == True:
            print(i, result[i])


topology_sort()
