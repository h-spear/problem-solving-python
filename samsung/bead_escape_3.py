# https://www.acmicpc.net/problem/15644

import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()
n, m = map(int, input().split())
graph = [list(input()) for _ in range(n)]
rx, ry = 0, 0
bx, by = 0, 0
gx, gy = 0, 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
hash = {0: "U", 1: "D", 2: "L", 3: "R"}
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
    nrx, nry = get_next_position(rx, ry, dir)
    nbx, nby = get_next_position(bx, by, dir)

    if rx == nrx and ry == nry and bx == nbx and by == nby:
        return None
    if nbx == gx and nby == gy:
        return None
    if nrx == gx and nry == gy:
        return True
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


def simulation(rx, ry, bx, by):
    answer = -1
    path = ""
    q = deque()
    q.append((rx, ry, bx, by, 1, ""))

    while q:
        rx, ry, bx, by, cnt, strpath = q.popleft()

        if cnt == 11:
            continue
        if answer != -1:
            break

        for i in range(4):
            res = incline(rx, ry, bx, by, i)
            if res == True:
                answer = cnt
                path = strpath + hash[i]
                break
            if not res:
                continue
            q.append((*res, cnt + 1, strpath + hash[i]))

    print(answer)
    if path:
        print(path)


simulation(rx, ry, bx, by)
