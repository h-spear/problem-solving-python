# https://www.acmicpc.net/problem/16234

from collections import deque
import sys

n, l, r = map(int, input().split())

graph = []
for i in range(n):
    input_data = list(map(int, sys.stdin.readline().rstrip().split()))
    graph.append(input_data)

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(x, y, visited):
    q = deque([(x, y)])
    group = [(x, y)]
    sum = graph[x][y]
    count = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= 0 and nx < n and ny >= 0 and ny < n:
                if (
                    (nx, ny) not in group
                    and (nx, ny) not in visited
                    and l <= abs(graph[nx][ny] - graph[x][y]) <= r
                ):
                    group.append((nx, ny))
                    q.append((nx, ny))
                    sum += graph[nx][ny]
                    count += 1

    pop = sum // count
    for x, y in group:
        visited.add((x, y))
        graph[x][y] = pop

    return 1


def needBFS(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < n and ny >= 0 and ny < n:
            if l <= abs(graph[nx][ny] - graph[x][y]) <= r:
                return True
    return False


total_count = 0

while True:
    visited = set()
    count = 0
    for i in range(n):
        for j in range(n):
            if (i, j) not in visited:
                if needBFS(i, j):
                    count += bfs(i, j, visited)
                else:
                    count += 1

    if count == n * n:
        break
    total_count += 1

print(total_count)
