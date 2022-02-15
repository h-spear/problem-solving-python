# https://www.acmicpc.net/problem/1944

from collections import deque

n, m = map(int, input().split())
graph = [list(input()) for _ in range(n)]
hash = dict()
edges = []
cnt = 0

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def labeling():
    global cnt
    for i in range(n):
        for j in range(n):
            if graph[i][j] == "1" or graph[i][j] == "0":
                continue
            cnt += 1
            hash[(i, j)] = cnt


def bfs(_x, _y):
    q = deque([(_x, _y)])
    visited = [[0] * n for _ in range(n)]
    visited[_x][_y] = 1
    while q:
        x, y = q.popleft()
        if graph[x][y] == "S" or graph[x][y] == "K":
            if _x == x and _y == y:
                pass
            else:
                edges.append((visited[x][y] - 1, hash[(_x, _y)], hash[(x, y)]))

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if graph[nx][ny] == "1":
                continue
            if visited[nx][ny]:
                continue
            visited[nx][ny] = visited[x][y] + 1
            q.append((nx, ny))


def make_edges():
    for i in range(n):
        for j in range(n):
            if graph[i][j] == "0":
                continue
            if graph[i][j] == "1":
                continue
            bfs(i, j)


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


def kruskal():
    parent = [i for i in range(cnt + 1)]
    edges.sort()
    answer = 0
    for c, a, b in edges:
        if find(parent, a) == find(parent, b):
            continue
        answer += c
        union(parent, a, b)

    for i in range(1, cnt + 1):
        find(parent, i)

    if sum(parent) == cnt:
        print(answer)
    else:
        print(-1)


labeling()
make_edges()
kruskal()
