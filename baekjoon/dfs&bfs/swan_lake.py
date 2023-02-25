# https://www.acmicpc.net/problem/3197
# 백조가 만날 수 있는지 여부를 union-find로 구현해야 시간초과를 통과할 수 있음

import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()
r, c = map(int, input().split())
graph = []
for _ in range(r):
    graph.append(list(input()))

parent = [i for i in range(r * c)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def init_parent(parent):
    visited = [[0] * c for _ in range(r)]

    def bfs(_x, _y):
        q = deque([(_x, _y)])
        visited[_x][_y] = 1
        while q:
            x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or ny < 0 or nx >= r or ny >= c:
                    continue
                if visited[nx][ny]:
                    continue
                if graph[nx][ny] == "X":
                    continue
                q.append((nx, ny))
                visited[nx][ny] = 1
                union(parent, _x * c + _y, nx * c + ny)

    for i in range(r):
        for j in range(c):
            if graph[i][j] == "X":
                continue
            if visited[i][j]:
                continue
            bfs(i, j)


def is_adjacent(x, y, graph):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or ny < 0 or nx >= r or ny >= c:
            continue
        if graph[nx][ny] == "." or graph[nx][ny] == "L":
            return 1
    return 0


def count_adjacent(graph):
    temp = []
    for i in range(r):
        for j in range(c):
            if is_adjacent(i, j, graph):
                temp.append((i, j))
    return temp


def find_swans(graph):
    pos = []

    for i in range(r):
        for j in range(c):
            if graph[i][j] == "L":
                pos.append(i)
                pos.append(j)
            if len(pos) == 4:
                return pos


def swan_meets(parent, ax, ay, bx, by):
    return find(parent, ax * c + ay) == find(parent, bx * c + by)


def melting(graph, adj_coord):
    removed = []
    temp = set()
    for x, y in adj_coord:
        removed.append((x, y))
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= r or ny >= c:
                continue
            if graph[nx][ny] == "X":
                temp.add((nx, ny))

    for x, y in removed:
        graph[x][y] = "."

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= r or ny >= c:
                continue
            if graph[nx][ny] == "X":
                continue
            union(parent, x * c + y, nx * c + ny)

    return list(temp)


def simulate():
    init_parent(parent)
    sx, sy, tx, ty = find_swans(graph)
    temp = count_adjacent(graph)
    days = 0

    while not swan_meets(parent, sx, sy, tx, ty):
        temp = melting(graph, temp)
        days += 1

    print(days)


simulate()
