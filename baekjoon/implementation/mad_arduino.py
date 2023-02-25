# https://www.acmicpc.net/problem/8972

import sys
from collections import Counter

input = lambda: sys.stdin.readline().rstrip()
r, c = map(int, input().split())
a_x, a_y = 0, 0
enemies = []
for i in range(r):
    input_data = list(input())
    for j, x in enumerate(input_data):
        if x == "I":
            a_x, a_y = i, j
        if x == "R":
            enemies.append((i, j))
commands = list(map(int, list(input())))

dx = [0, 1, 1, 1, 0, 0, 0, -1, -1, -1]
dy = [0, -1, 0, 1, -1, 0, 1, -1, 0, 1]

lose = False


def move_arduino(cmd):
    global a_x, a_y, lose
    a_x, a_y = a_x + dx[cmd], a_y + dy[cmd]

    if (a_x, a_y) in enemies:
        lose = True


def seek_position(x, y):
    global a_x, a_y
    min_dist = float("inf")
    cmd = 0
    for i in range(1, 10):
        nx = x + dx[i]
        ny = y + dy[i]

        cal = abs(nx - a_x) + abs(ny - a_y)
        if cal < min_dist:
            min_dist = cal
            cmd = i

    return x + dx[cmd], y + dy[cmd]


def move_mad_arduino():
    global enemies, lose, a_x, a_y
    tmp_pos = []
    for x, y in enemies:
        nx, ny = seek_position(x, y)
        tmp_pos.append((nx, ny))

    if (a_x, a_y) in tmp_pos:
        lose = True
        return

    enemies = []
    counter = Counter(tmp_pos)
    for pos in counter:
        if counter[pos] == 1:
            enemies.append(pos)


def print_field():
    graph = [["."] * c for _ in range(r)]
    graph[a_x][a_y] = "I"
    for x, y in enemies:
        graph[x][y] = "R"

    for row in graph:
        print("".join(row))


def simulate():
    for i, cmd in enumerate(commands):
        move_arduino(cmd)
        move_mad_arduino()
        if lose:
            print("kraj", i + 1)
            return
    print_field()


simulate()
