import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
h, w, s_r, s_c, f_r, f_c = map(int, input().split())

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def check_border(x, y):
    global w, h

    # horizontal
    for i in range(w):
        if graph[x][y + i] == 1 or graph[x + h - 1][y + i] == 1:
            return True

    # vertical
    for i in range(h):
        if graph[x + i][y] == 1 or graph[x + i][y + w - 1] == 1:
            return True
    return False


def bfs(x, y):
    q = deque([(x, y)])
    visited = [[0] * (m - w + 1) for _ in range(n - h + 1)]
    visited[x][y] = 1
    while q:
        x, y = q.popleft()

        if x == f_r - 1 and y == f_c - 1:
            return visited[x][y] - 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx > n - h or ny < 0 or ny > m - w:
                continue
            if visited[nx][ny]:
                continue
            if check_border(x, y):
                continue

            q.append((nx, ny))
            visited[nx][ny] = visited[x][y] + 1
    return -1


print(bfs(s_r - 1, s_c - 1))
