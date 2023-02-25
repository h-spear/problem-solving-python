# https://www.acmicpc.net/problem/17143

import sys

input = lambda: sys.stdin.readline().rstrip()
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
R, C, M = map(int, input().split())
shark = [[[] for _ in range(C)] for _ in range(R)]
pos = -1
answer = 0
for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    shark[r - 1][c - 1].append((z, s, d - 1))


def move_fisher():
    global pos
    pos += 1


def catch():
    global answer, pos
    for i in range(R):
        if shark[i][pos]:
            answer += shark[i][pos][0][0]
            shark[i][pos] = []
            return


def after_move(r, c, s, d, z):
    nr, nc = r, c
    if d <= 1:
        if s > (R - 1) * 2:
            s -= (R - 1) * 2

        for i in range(s):
            if nr + dx[d] < 0 or nr + dx[d] >= R:
                d = 1 - d
            nr += dx[d]
        return nr, nc, s, d, z
    else:
        if s > (C - 1) * 2:
            s -= (C - 1) * 2

        for i in range(s):
            if nc + dy[d] < 0 or nc + dy[d] >= C:
                d = 5 - d
            nc += dy[d]
        return nr, nc, s, d, z


def shark_move():
    global shark
    temp = [[[] for _ in range(C)] for _ in range(R)]
    for r in range(R):
        for c in range(C):
            for z, s, d in shark[r][c]:
                nr, nc, ns, nd, nz = after_move(r, c, s, d, z)
                temp[nr][nc].append((nz, ns, nd))

    for r in range(R):
        for c in range(C):
            if not temp[r][c]:
                continue

            temp[r][c].sort(reverse=True)
            temp[r][c] = [temp[r][c][0]]

    shark = temp


def simulate():
    for i in range(C):
        move_fisher()
        catch()
        shark_move()
    print(answer)


simulate()
