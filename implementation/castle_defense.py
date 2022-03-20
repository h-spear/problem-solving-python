# https://www.acmicpc.net/problem/17135
# simulation & bruteforce

import sys
from collections import deque
from itertools import combinations
from copy import deepcopy

input = lambda: sys.stdin.readline().rstrip()
dx = [0, -1, 0]
dy = [-1, 0, 1]
n, m, d = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
answer = 0


def get_target(graph, x, y):
    if graph[x][y] == 1:
        return (x, y)

    q = deque([(x, y, 1)])
    visited = [[0] * m for _ in range(n)]
    visited[x][y] = 1
    while q:
        x, y, cnt = q.popleft()

        if cnt >= d:
            continue

        for i in range(3):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or ny >= m:
                continue
            if visited[nx][ny] == 1:
                continue
            if graph[nx][ny] == 1:
                return (nx, ny)
            visited[nx][ny] = 1
            q.append((nx, ny, cnt + 1))

    return None


def simulate(graph, a, b, c):
    global answer
    cnt = 0
    for archer in range(n - 1, -1, -1):
        targets = set()
        for i in [a, b, c]:
            target = get_target(graph, archer, i)
            if target:
                targets.add(target)

        for x, y in targets:
            graph[x][y] = 0
            cnt += 1

    answer = max(answer, cnt)


for a, b, c in combinations(range(m), 3):
    simulate(deepcopy(graph), a, b, c)

print(answer)
