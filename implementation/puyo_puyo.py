# https://www.acmicpc.net/problem/11559

from collections import deque

graph = []
for _ in range(12):
    graph.append(list(input()))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(i, j):
    visited = [[0] * 6 for _ in range(12)]
    q = deque([(i, j)])
    visited[i][j] = 1
    color = graph[i][j]
    cnt = 1
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= 0 and nx < 12 and ny >= 0 and ny < 6:
                if not visited[nx][ny] and graph[nx][ny] == color:
                    cnt += 1
                    visited[nx][ny] = 1
                    q.append((nx, ny))

    if cnt >= 4:
        for i in range(12):
            for j in range(6):
                if visited[i][j] == 1:
                    graph[i][j] = "."
        return True
    return False


def gravity():
    for i in range(10, -1, -1):
        for j in range(6):
            if graph[i][j] != "." and graph[i + 1][j] == ".":
                for k in range(i + 1, 12):
                    if k == 11 and graph[k][j] == ".":
                        graph[k][j] = graph[i][j]
                    elif graph[k][j] != ".":
                        graph[k - 1][j] = graph[i][j]
                        break
                graph[i][j] = "."


def puyo():
    chain = False
    for i in range(12):
        for j in range(6):
            if graph[i][j] != ".":
                if bfs(i, j):
                    chain = True

    if chain:
        gravity()

    return chain


answer = 0
while puyo():
    answer += 1
print(answer)
