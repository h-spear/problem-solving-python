# https://www.acmicpc.net/problem/2252

import sys
from collections import deque

n, m = map(int, input().split())

indegree = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    data = list(map(int, sys.stdin.readline().rstrip().split()))
    graph[data[0]].append(data[1])
    indegree[data[1]] += 1

# topology sort
q = deque()

for i in range(1, n + 1):
    if indegree[i] == 0:
        q.append(i)

result = []
while q:
    now = q.popleft()
    result.append(now)

    for x in graph[now]:
        indegree[x] -= 1
        if indegree[x] == 0:
            q.append(x)

for x in result:
    print(x, end=" ")
