# https://www.acmicpc.net/problem/19236
import copy
from os import path

graph = [[None] * 4 for _ in range(4)]

for i in range(4):
    input_data = list(map(int, input().split()))
    for j in range(0, 8, 2):
        graph[i][j // 2] = [input_data[j], input_data[j + 1] - 1]


# Up, UL, Left, LD, Down, DR, Right, RU
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]


def turnLeft(direction):
    return (direction + 1) % 8


def findFish(graph, num):
    for i in range(4):
        for j in range(4):
            if graph[i][j][0] == num:
                return i, j
    return None


def fishMove(graph, now_x, now_y):
    for j in range(1, 17):
        fish = findFish(graph, j)
        if fish == None:
            continue
        x, y = fish
        dir = graph[x][y][1]
        for _ in range(8):
            nx = x + dx[dir]
            ny = y + dy[dir]

            if nx >= 0 and nx < 4 and ny >= 0 and ny < 4 and graph[nx][ny][0] != -1:
                if not (nx == now_x and ny == now_y):
                    graph[nx][ny], graph[x][y] = graph[x][y], graph[nx][ny]
                    break
            dir = turnLeft(dir)
    return graph


def possiblePath(shark_x, shark_y, shark_dir):
    path = []
    while True:
        shark_x = shark_x + dx[shark_dir]
        shark_y = shark_y + dy[shark_dir]
        if shark_x < 0 or shark_x >= 4 or shark_y < 0 or shark_y >= 4:
            break
        path.append((shark_x, shark_y))
    return path


result = 0


def dfs(graph, x, y, sum):
    global result
    graph = copy.deepcopy(graph)
    sum += graph[x][y][0]
    graph[x][y][0] = -1
    direction = graph[x][y][1]
    fishMove(graph, x, y)

    path = possiblePath(x, y, direction)
    if len(path) == 0:
        result = max(result, sum)
        return
    for next_x, next_y in path:
        dfs(graph, next_x, next_y, sum)


dfs(graph, 0, 0, 0)
print(result)
