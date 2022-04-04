# https://www.acmicpc.net/problem/1113

import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()
n, m = map(int, input().split())
graph = []
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
for _ in range(n):
    graph.append(list(map(int, list(input()))))


def bfs(x, y, h, visited):
    q = deque([(x, y)])
    visited[x][y] = 1
    path = [(x, y)]
    flag = False
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                flag = True
                continue
            if visited[nx][ny]:
                continue
            if graph[nx][ny] > h:
                continue

            visited[nx][ny] = 1
            path.append((nx, ny))
            q.append((nx, ny))

    if flag:
        return 0
    else:
        cnt = 0
        for x, y in path:
            graph[x][y] += 1
            cnt += 1
        return cnt


def simulation_height(h):
    visited = [[0] * m for _ in range(n)]
    result = 0
    for i in range(n):
        for j in range(m):
            if visited[i][j]:
                continue
            if graph[i][j] > h:
                continue
            result += bfs(i, j, h, visited)

    return result


def simulation():
    answer = 0
    for h in range(1, 10):
        answer += simulation_height(h)
    print(answer)


simulation()
