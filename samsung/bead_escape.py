# https://www.acmicpc.net/problem/13459

import sys

input = lambda: sys.stdin.readline().rstrip()
n, m = map(int, input().split())
graph = [list(input()) for _ in range(n)]
rx, ry = 0, 0
bx, by = 0, 0
gx, gy = 0, 0
answer = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for i in range(n):
    for j in range(m):
        if graph[i][j] == "B":
            bx, by = i, j
        if graph[i][j] == "R":
            rx, ry = i, j
        if graph[i][j] == "O":
            gx, gy = i, j


def get_next_position(x, y, dir):
    nx = x + dx[dir]
    ny = y + dy[dir]
    while 0 <= nx < n and 0 <= ny < m:
        if graph[nx][ny] == "O":
            return nx, ny
        if graph[nx][ny] == "#":
            return nx - dx[dir], ny - dy[dir]
        nx += dx[dir]
        ny += dy[dir]


def incline(rx, ry, bx, by, dir):
    global answer
    nrx, nry = get_next_position(rx, ry, dir)
    nbx, nby = get_next_position(bx, by, dir)

    if rx == nrx and ry == nry and bx == nbx and by == nby:
        return None
    if nbx == gx and nby == gy:
        return None
    if nrx == gx and nry == gy:
        answer = 1
        return None
    if nrx == nbx and nry == nby:
        if dir == 0:
            if rx < bx:
                nbx += 1
            else:
                nrx += 1
        elif dir == 1:
            if rx < bx:
                nrx -= 1
            else:
                nbx -= 1
        elif dir == 2:
            if ry < by:
                nby += 1
            else:
                nry += 1
        elif dir == 3:
            if ry < by:
                nry -= 1
            else:
                nby -= 1
    if rx == nrx and ry == nry and bx == nbx and by == nby:
        return None

    return (nrx, nry, nbx, nby)


def simulation(rx, ry, bx, by, depth=0):
    if depth == 10:
        return

    for i in range(4):
        if not answer:
            res = incline(rx, ry, bx, by, i)
            if not res:
                continue
            simulation(*res, depth + 1)


simulation(rx, ry, bx, by)
print(answer)
