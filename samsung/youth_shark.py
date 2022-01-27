# https://www.acmicpc.net/problem/19236

from copy import deepcopy

graph = []
for _ in range(4):
    input_data = list(map(int, input().split()))
    row = []
    for i in range(0, 8, 2):
        row.append((input_data[i], input_data[i + 1] - 1))
    graph.append(row)

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]


def find_obj(graph, num):
    for i in range(4):
        for j in range(4):
            if graph[i][j][0] == num:
                return (i, j)
    return None


def fish_move(graph, num=0):
    if num == 17:
        return

    coord = find_obj(graph, num)
    if not coord:
        fish_move(graph, num + 1)
        return

    x, y = coord
    dir = graph[x][y][1]
    for i in range(8):
        if x == y == -1:
            break

        next_dir = (dir + i) % 8
        nx = x + dx[next_dir]
        ny = y + dy[next_dir]

        if nx < 0 or nx >= 4 or ny < 0 or ny >= 4:
            continue
        if graph[nx][ny][0] == 99:
            continue

        graph[x][y] = (num, next_dir)
        graph[nx][ny], graph[x][y] = graph[x][y], graph[nx][ny]
        break

    fish_move(graph, num + 1)


def next_pos(graph):
    coord = find_obj(graph, 99)
    x, y = coord
    pos = []

    dir = graph[x][y][1]
    for i in range(1, 4):
        nx = x + dx[dir] * i
        ny = y + dy[dir] * i

        if nx < 0 or nx >= 4 or ny < 0 or ny >= 4:
            continue
        if graph[nx][ny][0] == -1:
            continue

        pos.append((nx, ny))
    return pos


def simulate(graph, x, y, score):
    global result
    copied = deepcopy(graph)
    num, dir = copied[x][y]
    score += num
    copied[x][y] = (99, dir)

    fish_move(copied)

    candidate = next_pos(copied)

    if len(candidate) == 0:
        result = max(result, score)
        return

    copied[x][y] = (-1, -1)
    #
    for nx, ny in candidate:
        simulate(copied, nx, ny, score)


result = 0
simulate(graph, 0, 0, 0)
print(result)
