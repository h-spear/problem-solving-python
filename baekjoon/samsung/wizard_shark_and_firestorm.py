# https://www.acmicpc.net/problem/20058

import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
n, q = map(int, input().split())
graph_length = 2 ** n
graph = [list(map(int, input().split())) for _ in range(graph_length)]
Lq = list(map(int, input().split()))


def rotate_matrix_90(A):
    n = len(A)  # length of row
    m = len(A[0])  # length of column
    result = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[j][n - i - 1] = A[i][j]
    return result


def storm(x, y, length, L):
    if L == 0:
        return

    if length == 2 ** L:
        temp = [[0] * length for _ in range(length)]
        for i in range(length):
            for j in range(length):
                temp[i][j] = graph[x + i][y + j]

        temp = rotate_matrix_90(temp)

        for i in range(length):
            for j in range(length):
                graph[x + i][y + j] = temp[i][j]
        return

    nn = length // 2
    storm(x, y, nn, L)
    storm(x, y + nn, nn, L)
    storm(x + nn, y, nn, L)
    storm(x + nn, y + nn, nn, L)


def count_adjacent_side(x, y):
    cnt = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= graph_length or ny >= graph_length:
            continue
        if graph[nx][ny] == 0:
            continue
        cnt += 1
    return cnt


def fire(length):
    temp = set()
    for i in range(length):
        for j in range(length):
            if graph[i][j] == 0:
                continue
            if count_adjacent_side(i, j) < 3:
                temp.add((i, j))

    for x, y in temp:
        if graph[x][y] != 0:
            graph[x][y] -= 1


def fire_storm(L):
    storm(0, 0, graph_length, L)
    fire(graph_length)


def bfs(x, y, visited):
    q = deque([(x, y)])
    visited[x][y] = 1
    cnt = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= graph_length or ny >= graph_length:
                continue
            if visited[nx][ny]:
                continue
            if graph[nx][ny] == 0:
                continue

            cnt += 1
            q.append((nx, ny))
            visited[nx][ny] = 1
    return cnt


def find_largest_chunk():
    result = 0
    visited = [[0] * graph_length for _ in range(graph_length)]
    for i in range(graph_length):
        for j in range(graph_length):
            if visited[i][j]:
                continue
            if graph[i][j] == 0:
                continue
            result = max(result, bfs(i, j, visited))
    return result


def calc_total_sum():
    result = 0
    for x in graph:
        result += sum(x)
    return result


def simul(Lq):
    for L in Lq:
        fire_storm(L)

    total = calc_total_sum()
    size = find_largest_chunk()
    print(total)
    print(size)


simul(Lq)
