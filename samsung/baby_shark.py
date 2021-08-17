# https://www.acmicpc.net/problem/16236

from collections import deque
import sys

n = int(input())

graph = []
shark_x, shark_y = 0, 0
for i in range(n):
    data = list(map(int, sys.stdin.readline().rstrip().split()))
    graph.append(data)
    for j in range(n):
        if graph[i][j] == 9:
            shark_x = i
            shark_y = j
            graph[i][j] = 0


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
size = 2


def bfs(x, y):
    global size
    q = deque([(0, x, y)])
    visited = [(x, y)]
    eatable = []
    while q:
        dist, x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= 0 and nx < n and ny >= 0 and ny < n and (nx, ny) not in visited:
                if graph[nx][ny] <= size:
                    visited.append((nx, ny))
                    q.append((dist + 1, nx, ny))
                    if graph[nx][ny] != 0 and graph[nx][ny] < size:
                        eatable.append((dist + 1, nx, ny))

    eatable.sort()
    return None if eatable == [] else eatable[0]


count = 0
result = 0
while True:
    eatable = bfs(shark_x, shark_y)
    if eatable == None:
        break
    time, shark_x, shark_y = eatable
    graph[shark_x][shark_y] = 0
    count += 1
    result += time

    if count == size:
        count = 0
        size += 1


print(result)
