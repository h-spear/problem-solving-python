# https://www.acmicpc.net/problem/16918

import sys

input = lambda: sys.stdin.readline().rstrip()

graph = []

r, c, n = map(int, input().split())
for _ in range(r):
    graph.append(list(input()))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def next_graph(bombs):
    next_graph = [["O"] * c for _ in range(r)]
    for x, y in bombs:
        next_graph[x][y] = "."

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= r or ny >= c:
                continue
            next_graph[nx][ny] = "."

    return next_graph


def bombs(graph):
    bombs = []
    for i in range(r):
        for j in range(c):
            if graph[i][j] != "O":
                continue
            bombs.append((i, j))
    return bombs


# n == 1인 경우와 n % 4 == 1인 경우가 다른 케이스가 존재함
if n == 1:
    graph = graph
elif n % 2 == 0:
    graph = [["O"] * c for _ in range(r)]
elif n % 4 == 3:
    graph = next_graph(bombs(graph))
elif n % 4 == 1:
    for _ in range(2):
        graph = next_graph(bombs(graph))


for x in graph:
    print("".join(x))
