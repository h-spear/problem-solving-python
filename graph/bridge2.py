# https://www.acmicpc.net/problem/17472
# BFS + MST

from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
edges = []
INF = int(1e5)
distance = [[INF] * (7) for _ in range(7)]
cnt = 0
parent = [i for i in range(7)]
answer = 0

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


def bfs(x, y, num):
    q = deque([(x, y)])
    visited[x][y] = num
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if graph[nx][ny] == 0:
                continue
            if visited[nx][ny]:
                continue
            q.append((nx, ny))
            visited[nx][ny] = num


def clustering():
    global cnt
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                continue
            if visited[i][j]:
                continue
            cnt += 1
            bfs(i, j, cnt)


def calc_dist(x, y):
    i1 = visited[x][y]
    for i in range(4):
        cnt = 0
        nx = x + dx[i]
        ny = y + dy[i]
        while 1:
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                break
            if visited[nx][ny] == i1:
                break
            if visited[nx][ny] != 0:
                if cnt < 2:
                    break

                i2 = visited[nx][ny]
                distance[i1][i2] = min(distance[i1][i2], cnt)
                break

            nx += dx[i]
            ny += dy[i]
            cnt += 1


def make_distance_vec():
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                continue
            if visited[i][j] == 0:
                continue
            calc_dist(i, j)


def make_edges():
    for i in range(1, cnt + 1):
        for j in range(i, cnt + 1):
            if distance[i][j] == INF:
                continue
            edges.append((distance[i][j], i, j))


def kruskal():
    global answer, cnt
    bridge = 0
    edges.sort()

    for edge in edges:
        dist, a, b = edge
        if find(parent, a) == find(parent, b):
            continue
        bridge += 1
        answer += dist
        union(parent, a, b)
        if bridge == cnt - 1:
            break

    if bridge != cnt - 1:
        answer = -1


clustering()
make_distance_vec()
make_edges()
kruskal()
print(answer)
