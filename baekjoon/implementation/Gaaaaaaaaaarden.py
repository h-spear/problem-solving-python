# https://www.acmicpc.net/problem/18809

import sys
from collections import deque
from itertools import combinations

input = lambda: sys.stdin.readline().rstrip()
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
n, m, g, r = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))


def bfs(candidate):
    cnt = 0
    q = deque(candidate)
    visited = [[[0, 0] for _ in range(m)] for _ in range(n)]
    for x, y, color in candidate:
        visited[x][y][color] = 1

    while q:
        for _ in range(len(q)):
            x, y, color = q.popleft()

            if x == y == color == -1:
                continue

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or ny < 0 or nx >= n or ny >= m:
                    continue
                if graph[nx][ny] == 0:
                    continue
                if visited[nx][ny][color]:
                    continue
                q.append((nx, ny, color))
                visited[nx][ny][color] = visited[x][y][color] + 1

        for i, (x, y, color) in enumerate(q):
            if visited[x][y][0] == visited[x][y][1]:
                q[i] = (-1, -1, -1)
                cnt += 1
    return cnt // 2


def simulation():
    answer = 0
    start = []
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 2:
                start.append((i, j))

    for selected in combinations(start, g + r):
        selected = set(selected)
        for selected_green in combinations(selected, g):
            selected_green = set(selected_green)
            selected_red = selected - selected_green

            candidate = []
            for x, y in selected_green:
                candidate.append((x, y, 0))
            for x, y in selected_red:
                candidate.append((x, y, 1))

            cnt = bfs(candidate)
            answer = max(answer, cnt)
    print(answer)


simulation()
