# https://www.acmicpc.net/problem/3665

import sys
from collections import deque

for tc in range(int(input())):
    n = int(input())

    graph = [[False] * (n + 1) for _ in range(n + 1)]
    indegree = [0] * (n + 1)
    input_data = list(map(int, sys.stdin.readline().rstrip().split()))
    for i in range(n):
        for j in range(i + 1, n):
            graph[input_data[i]][input_data[j]] = True
            indegree[input_data[j]] += 1

    m = int(input())
    for i in range(m):
        a, b = map(int, sys.stdin.readline().rstrip().split())

        if graph[a][b]:
            graph[a][b] = False
            graph[b][a] = True
            indegree[a] += 1
            indegree[b] -= 1
        else:
            graph[a][b] = True
            graph[b][a] = False
            indegree[a] -= 1
            indegree[b] += 1

    result = []
    q = deque()

    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    certain = True
    cycle = False

    for i in range(n):
        # 큐의 원소가 없으면 cycle
        if len(q) == 0:
            cycle = True
            break
        # 큐의 원소가 2개 이상이면 여러 경우 가능
        if len(q) >= 2:
            certain = False
            break

        now = q.popleft()
        result.append(now)

        for j in range(1, n + 1):
            if graph[now][j]:
                indegree[j] -= 1
                if indegree[j] == 0:
                    q.append(j)

    if cycle:
        print("IMPOSSIBLE")
    elif not certain:
        print("?")
    else:
        for i in result:
            print(i, end=" ")
        print()
