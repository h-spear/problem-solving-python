# https://www.acmicpc.net/problem/2174
# 좌표계가 달라서 헷갈림

import sys

input = lambda: sys.stdin.readline().rstrip()
a, b = map(int, input().split())
n, m = map(int, input().split())
graph = [[0] * a for _ in range(b)]
robot = {}
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
hash = {s: i for i, s in enumerate("NESW")}
command = []

for i in range(1, n + 1):
    y, x, d = input().split()
    x = b - int(x)
    y = int(y) - 1
    graph[x][y] = i
    robot[i] = [x, y, hash[d]]

for _ in range(m):
    command.append(list(input().split()))


def func(rb, cmd, repeat):
    x, y, d = robot[rb]
    if cmd == "L":
        repeat %= 4
        robot[rb][2] = (d - repeat) % 4
    elif cmd == "R":
        repeat %= 4
        robot[rb][2] = (d + repeat) % 4
    else:
        for _ in range(repeat):
            nx = x + dx[d]
            ny = y + dy[d]

            if nx < 0 or ny < 0 or nx >= b or ny >= a:
                print("Robot {} crashes into the wall".format(rb))
                return True
            if graph[nx][ny] != 0:
                print("Robot {} crashes into robot {}".format(rb, graph[nx][ny]))
                return True

            robot[rb] = [nx, ny, d]
            graph[nx][ny] = rb
            graph[x][y] = 0
            x = nx
            y = ny

    return False


def simul():
    for rb, cmd, repeat in command:
        rb = int(rb)
        repeat = int(repeat)
        crash = func(rb, cmd, repeat)
        if crash:
            return
    print("OK")


simul()
