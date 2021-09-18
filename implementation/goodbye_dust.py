# https://www.acmicpc.net/problem/17144
# pypy3

import sys

input = lambda: sys.stdin.readline().rstrip()

r, c, t = map(int, input().split())
graph = []

cleaner = (0, 0)

for i in range(r):
    input_data = list(map(int, (input().split())))
    graph.append(input_data)
    for j in range(c):
        if input_data[j] == -1:
            cleaner = (i - 1, j)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def findDust():
    dust = []
    for i in range(r):
        for j in range(c):
            if graph[i][j] > 0:
                dust.append((i, j))
    return dust


def afterDust():
    temp = [[0] * c for _ in range(r)]
    temp_dust = []
    dust = findDust()
    for x, y in dust:
        cnt = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= 0 and nx < r and ny >= 0 and ny < c:
                if graph[nx][ny] != -1:
                    temp[nx][ny] += graph[x][y] // 5
                    cnt += 1
                    temp_dust.append((nx, ny))

        temp[x][y] -= graph[x][y] // 5 * cnt

    for i in range(r):
        for j in range(c):
            graph[i][j] += temp[i][j]


def clockwise():
    global r, c
    x, y = cleaner
    for target_c in range(y, -1, -1):
        if target_c - 1 >= 0:
            graph[x][target_c] = graph[x][target_c - 1]
    for target_r in range(x, -1, -1):
        if target_r - 1 >= 0:
            graph[target_r][0] = graph[target_r - 1][0]
    for target_c in range(0, c):
        if target_c + 1 < c:
            graph[0][target_c] = graph[0][target_c + 1]
    for target_r in range(0, x):
        if target_r + 1 < r:
            graph[target_r][c - 1] = graph[target_r + 1][c - 1]
    for target_c in range(c - 1, y, -1):
        if target_c - 1 >= 0:
            graph[x][target_c] = graph[x][target_c - 1]
    graph[x][y] = -1
    if y + 1 < r:
        graph[x][y + 1] = 0


def counterclockwise():
    global r, c
    x, y = cleaner[0] + 1, cleaner[1]
    for target_c in range(y, -1, -1):
        if target_c - 1 >= 0:
            graph[x][target_c] = graph[x][target_c - 1]
    for target_r in range(x, r):
        if target_r + 1 < r:
            graph[target_r][0] = graph[target_r + 1][0]
    for target_c in range(0, c):
        if target_c + 1 < c:
            graph[r - 1][target_c] = graph[r - 1][target_c + 1]
    for target_r in range(r - 1, x, -1):
        if target_r - 1 < r:
            graph[target_r][c - 1] = graph[target_r - 1][c - 1]
    for target_c in range(c - 1, y, -1):
        if target_c - 1 >= 0:
            graph[x][target_c] = graph[x][target_c - 1]
    graph[x][y] = -1
    if y + 1 < r:
        graph[x][y + 1] = 0


def simulation():
    for i in range(t):
        afterDust()
        clockwise()
        counterclockwise()

    answer = 0

    for i in range(r):
        for j in range(c):
            if graph[i][j] != -1:
                answer += graph[i][j]

    return answer


print(simulation())
