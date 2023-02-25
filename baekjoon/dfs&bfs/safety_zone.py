# https://www.acmicpc.net/problem/2468

import sys
from collections import deque

graph = []
n = int(input())
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().rstrip().split())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# ** vistied를 행렬로 나타내는 것이 시간이 더 적게 걸림 **
visited = [[False] * n for _ in range(n)]


def bfs(x, y, h):
    global visited
    q = deque([(x, y)])
    visited[x][y] = True
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= 0 and nx < n and ny >= 0 and ny < n:
                if graph[nx][ny] > h and visited[nx][ny] == False:
                    visited[nx][ny] = True
                    q.append((nx, ny))
    return 1


def maxHeight():
    height = set()
    for i in range(n):
        for j in range(n):
            height.add(graph[i][j])
    return list(height)


result = 1
for k in maxHeight():
    count = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] > k and visited[i][j] == False:
                count += bfs(i, j, k)
    result = max(result, count)
    visited = [[False] * n for _ in range(n)]

print(result)
