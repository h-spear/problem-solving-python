# https://www.acmicpc.net/problem/15683
# dfs

from copy import deepcopy

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
iteration = [0, 4, 2, 4, 4, 1]

answer = 10000
# up, right, down, left
def watch(graph, x, y, dir):
    nx, ny = x, y
    graph[nx][ny] = 9
    while 1:
        nx = nx + dx[dir]
        ny = ny + dy[dir]

        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            return

        if graph[nx][ny] >= 1 and graph[nx][ny] <= 5:
            continue

        if graph[nx][ny] == 6:
            return

        graph[nx][ny] = 9


def peek(graph):
    for i in range(n):
        for j in range(m):
            if 1 <= graph[i][j] <= 5:
                return (i, j)
    return (-1, -1)


def count(graph):
    global answer
    cnt = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                cnt += 1
    answer = min(answer, cnt)


def dfs(graph):
    x, y = peek(graph)
    cctv = graph[x][y]

    if x == y == -1:
        count(graph)
        return

    for dir in range(iteration[graph[x][y]]):
        graph_copy = deepcopy(graph)

        if cctv == 1:
            watch(graph_copy, x, y, dir)
        elif cctv == 2:
            watch(graph_copy, x, y, dir)
            watch(graph_copy, x, y, dir + 2)
        elif cctv == 3:
            watch(graph_copy, x, y, dir)
            watch(graph_copy, x, y, (dir + 1) % 4)
        elif cctv == 4:
            watch(graph_copy, x, y, dir)
            watch(graph_copy, x, y, (dir + 1) % 4)
            watch(graph_copy, x, y, (dir + 3) % 4)
        elif cctv == 5:
            watch(graph_copy, x, y, 0)
            watch(graph_copy, x, y, 1)
            watch(graph_copy, x, y, 2)
            watch(graph_copy, x, y, 3)

        dfs(graph_copy)


dfs(graph)
print(answer)
