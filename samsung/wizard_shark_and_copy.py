# https://www.acmicpc.net/problem/23290

import sys
from copy import deepcopy

input = lambda: sys.stdin.readline().rstrip()
m, s = map(int, input().split())
fish = [[[] for _ in range(4)] for _ in range(4)]
smell = [[0] * 4 for _ in range(4)]
for _ in range(m):
    fx, fy, d = map(int, input().split())
    fish[fx - 1][fy - 1].append(d - 1)

sx, sy = map(int, input().split())
sx -= 1
sy -= 1
dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
d_rev = {0: 4, 2: 6, 4: 0, 6: 2}
max_cnt = -1
path = ""


def copy_magic_cast(fish):
    return deepcopy(fish)


def fish_move():
    global fish
    temp = [[[] for _ in range(4)] for _ in range(4)]
    for i in range(4):
        for j in range(4):
            while fish[i][j]:
                d = fish[i][j].pop()
                moved = False
                for k in range(8):
                    nd = (d - k) % 8
                    nx = i + dx[nd]
                    ny = j + dy[nd]
                    if nx == sx and ny == sy:
                        continue
                    if nx < 0 or ny < 0 or nx >= 4 or ny >= 4:
                        continue
                    if smell[nx][ny]:
                        continue
                    moved = True
                    temp[nx][ny].append(nd)
                    break
                if not moved:
                    temp[i][j].append(d)

    fish = temp


def search_path(x, y, depth=0, str_path=""):
    global path, max_cnt
    if depth == 3:
        temp = set([(x, y)])
        for i in [2, 1]:
            d = d_rev[int(str_path[i])]
            x += dx[d]
            y += dy[d]
            temp.add((x, y))

        cnt = 0
        for x, y in temp:
            cnt += len(fish[x][y])

        if cnt > max_cnt:
            max_cnt = cnt
            path = str_path
        return

    for i in [2, 0, 6, 4]:
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or ny < 0 or nx >= 4 or ny >= 4:
            continue
        search_path(nx, ny, depth + 1, str_path + str(i))


def shark_move():
    global sx, sy, max_cnt
    max_cnt = -1
    search_path(sx, sy)
    for p in path:
        p = int(p)
        nx = sx + dx[p]
        ny = sy + dy[p]
        if fish[nx][ny]:
            fish[nx][ny] = []
            smell[nx][ny] = 3
        sx, sy = nx, ny


def remove_smell():
    for i in range(4):
        for j in range(4):
            smell[i][j] = max(smell[i][j] - 1, 0)


def copy_magic(copied):
    for i in range(4):
        for j in range(4):
            fish[i][j].extend(copied[i][j])


def count_fish():
    counter = 0
    for i in range(4):
        for j in range(4):
            counter += len(fish[i][j])
    return counter


def simulation():
    for i in range(s):
        copied = copy_magic_cast(fish)
        fish_move()
        shark_move()
        remove_smell()
        copy_magic(copied)

    answer = count_fish()
    print(answer)


simulation()
