# https://www.acmicpc.net/problem/4179

from collections import deque
import sys

input = lambda: sys.stdin.readline().rstrip()

r, c = map(int, input().split())
graph = [list(input()) for _ in range(r)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(x, y, q_fire: deque):
    q = deque([(x, y, 0)])
    visited = [[0] * c for _ in range(r)]
    visited[x][y] = 1

    visited_fire = [[0] * c for _ in range(r)]
    for _x, _y, _ in q_fire:
        visited_fire[_x][_y] = 1

    while q:
        x, y, t = q.popleft()

        # fire spread
        while len(q_fire) and q_fire[0][2] == t:
            f_x, f_y, f_t = q_fire.popleft()

            for i in range(4):
                nfx = f_x + dx[i]
                nfy = f_y + dy[i]

                if nfx < 0 or nfx >= r or nfy < 0 or nfy >= c:
                    continue
                if visited_fire[nfx][nfy]:
                    continue
                if graph[nfx][nfy] == "#":
                    continue
                if graph[nfx][nfy] == "F":
                    continue
                visited_fire[nfx][nfy] = 1
                graph[nfx][nfy] = "F"
                q_fire.append((nfx, nfy, f_t + 1))

        if (x == 0 or y == 0 or x == r - 1 or y == c - 1) and graph[x][y] != "F":
            return t + 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= r or ny < 0 or ny >= c:
                continue
            if visited[nx][ny]:
                continue
            if graph[nx][ny] == "#":
                continue
            if graph[nx][ny] == "F":
                continue
            visited[nx][ny] = 1
            q.append((nx, ny, t + 1))
    return "IMPOSSIBLE"


x, y, fire = 0, 0, deque()

for i in range(r):
    for j in range(c):
        if graph[i][j] == "F":
            fire.append((i, j, 1))
        if graph[i][j] == "J":
            graph[i][j] = "."
            x, y = i, j

print(bfs(x, y, fire))
