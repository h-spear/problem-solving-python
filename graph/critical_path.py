# https://www.acmicpc.net/problem/1948

import sys
from collections import deque, defaultdict

input = lambda: sys.stdin.readline().rstrip()

n = int(input())
m = int(input())
graph = defaultdict(list)
graph_rev = defaultdict(list)
time = [0] * (n + 1)
in_degree = [0] * (n + 1)
result = [0] * (n + 1)
done = [0] * (n + 1)
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph_rev[b].append((a, c))
    in_degree[b] += 1
start, end = map(int, input().split())


def topology_sort():
    q = deque()
    cnt = 0
    for i in range(1, n + 1):
        if in_degree[i] == 0:
            q.append(i)

    while q:
        x = q.popleft()
        for y, time in graph[x]:
            in_degree[y] -= 1
            result[y] = max(result[y], result[x] + time)
            if in_degree[y] == 0:
                q.append(y)

    q.append(end)
    while q:
        x = q.popleft()

        for y, time in graph_rev[x]:
            if result[x] - result[y] == time:
                cnt += 1
                if done[y] == 0:
                    q.append(y)
                    done[y] = 1

    print(result[end])
    print(cnt)


topology_sort()
