# https://www.acmicpc.net/problem/2151

from collections import deque

n = int(input())
graph = [list(input()) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(x, y, target_x, target_y):
    q = deque([(x, y)])
    visited = [[0] * n for _ in range(n)]
    visited[x][y] = 1
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x
            ny = y

            while 0 <= nx + dx[i] < n and 0 <= ny + dy[i] < n:
                nx += dx[i]
                ny += dy[i]

                if graph[nx][ny] == "*":
                    break
                if graph[nx][ny] == "!" and not visited[nx][ny]:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))
                if nx == target_x and ny == target_y:
                    print(visited[x][y] - 1)
                    return
    return


coord = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == "#":
            coord.append(i)
            coord.append(j)
bfs(*coord)
