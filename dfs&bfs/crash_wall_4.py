# https://www.acmicpc.net/problem/16946

import sys
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


input = lambda: sys.stdin.readline().rstrip()
n, m = map(int, input().split())
graph = [list(map(int, list(input()))) for _ in range(n)]
group = [[0] * m for _ in range(n)]
area = {}


def grouping(x, y, num):
    q = deque([(x, y)])
    group[x][y] = num
    cnt = 1
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if graph[nx][ny] == 1:
                continue
            if group[nx][ny]:
                continue
            q.append((nx, ny))
            group[nx][ny] = num
            cnt += 1
    area[num] = cnt


def calc_movable(x, y):
    adjacent = set()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue
        if group[nx][ny] == 0:
            continue
        adjacent.add(group[nx][ny])

    cnt = 1
    for num in adjacent:
        cnt += area[num]
    return cnt % 10


num = 1
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0 and group[i][j] == 0:
            grouping(i, j, num)
            num += 1

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            graph[i][j] = calc_movable(i, j)

for i in range(n):
    for j in range(m):
        print(graph[i][j], end="")
    print()
