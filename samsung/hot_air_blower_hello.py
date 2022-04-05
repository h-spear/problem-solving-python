# https://www.acmicpc.net/problem/23289

import sys
from collections import defaultdict

input = lambda: sys.stdin.readline().rstrip()
r, c, k = map(int, input().split())
graph = []
for _ in range(r):
    graph.append(list(map(int, input().split())))
w = int(input())
wall = defaultdict(list)
chocolate = 0
blower = []
inspect_area = []

# right, left, up, down
dir = [(0, 1), (0, -1), (-1, 0), (1, 0)]
dx = [[-1, 0, 1], [-1, 0, 1], [-1, -1, -1], [1, 1, 1]]
dy = [[1, 1, 1], [-1, -1, -1], [-1, 0, 1], [-1, 0, 1]]
check_list = [
    [(2, 0), (0, -1), (3, 0)],
    [(2, 1), (1, -1), (3, 1)],
    [(1, 2), (2, -1), (0, 2)],
    [(1, 3), (3, -1), (0, 3)],
]


def initialization():
    for i in range(r):
        for j in range(c):
            if graph[i][j] == 5:
                inspect_area.append((i, j))
            elif graph[i][j] >= 1:
                blower.append((i, j, graph[i][j] - 1))
            graph[i][j] = 0

    for _ in range(w):
        x, y, t = map(int, input().split())
        wall[(x - 1, y - 1)].append(t)


def valid_position(x, y):
    if x < 0 or y < 0 or x >= r or y >= c:
        return False
    return True


def stuck_in_the_wall(x, y, d):
    if d == 0:
        return 1 in wall[(x, y)]
    elif d == 1:
        return 1 in wall[(x, y - 1)]
    elif d == 2:
        return 0 in wall[(x, y)]
    elif d == 3:
        return 0 in wall[(x + 1, y)]


def blow_possible(x, y, d, i):
    fi, se = check_list[d][i]
    if stuck_in_the_wall(x, y, fi):
        return False
    x += dir[fi][0]
    y += dir[fi][1]

    if stuck_in_the_wall(x, y, se):
        return False
    return True


def blow_warm_air(x, y, d, temperature=5, visited=None):
    if temperature == 0:
        return
    if temperature == 5:
        visited = [[0] * c for _ in range(r)]
        x += dx[d][1]
        y += dy[d][1]

    graph[x][y] += temperature
    visited[x][y] = 1

    for i in range(3):
        nx = x + dx[d][i]
        ny = y + dy[d][i]

        if not valid_position(nx, ny):
            continue
        if visited[nx][ny]:
            continue
        if not blow_possible(x, y, d, i):
            continue
        blow_warm_air(nx, ny, d, temperature - 1, visited)


def temperature_control():
    temp = [[0] * c for _ in range(r)]
    for x in range(r):
        for y in range(c):
            for i in range(4):
                _dx, _dy = dir[i]
                nx = x + _dx
                ny = y + _dy

                if not valid_position(nx, ny):
                    continue
                if stuck_in_the_wall(x, y, i):
                    continue

                diff = abs(graph[x][y] - graph[nx][ny]) // 4
                if graph[x][y] > graph[nx][ny]:
                    temp[x][y] -= diff
                    temp[nx][ny] += diff
                else:
                    temp[x][y] += diff
                    temp[nx][ny] -= diff

    for i in range(r):
        for j in range(c):
            graph[i][j] += temp[i][j] // 2


def outside_temperature_down():
    for i in range(r):
        graph[i][0] = max(graph[i][0] - 1, 0)
        graph[i][c - 1] = max(graph[i][c - 1] - 1, 0)

    for j in range(1, c - 1):
        graph[0][j] = max(graph[0][j] - 1, 0)
        graph[r - 1][j] = max(graph[r - 1][j] - 1, 0)


def eat_chocolate():
    global chocolate
    chocolate += 1


def inspect():
    for x, y in inspect_area:
        if graph[x][y] < k:
            return False
    return True


def simulation():
    initialization()
    while 1:
        for x, y, d in blower:
            blow_warm_air(x, y, d)

        temperature_control()
        outside_temperature_down()
        eat_chocolate()
        result = inspect()

        if chocolate > 100:
            print(101)
            return
        if result == True:
            print(chocolate)
            break


simulation()
