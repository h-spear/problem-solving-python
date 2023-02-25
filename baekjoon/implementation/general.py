# https://www.acmicpc.net/problem/16509

from collections import deque

r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())

cond_dx = [-1, -1, 0, 0, 1, 1, 0, 0]
cond_dy = [0, 0, -1, -1, 0, 0, 1, 1]
cond_dx2 = [-2, -2, 1, -1, 2, 2, 1, -1]
cond_dy2 = [-1, 1, -2, -2, 1, -1, 2, 2]
dx = [-3, -3, 2, -2, 3, 3, 2, -2]
dy = [2, -2, -3, -3, 2, -2, 3, 3]


def is_valid_pos(x, y):
    if x < 0 or y < 0 or x >= 10 or y >= 9:
        return False
    return True


def bfs(x, y):
    q = deque([(x, y)])
    visited = [[0] * 9 for _ in range(10)]
    visited[x][y] = 1
    while q:
        x, y = q.popleft()

        if x == r2 and y == c2:
            print(visited[x][y] - 1)
            return

        for i in range(8):
            cond_x1 = x + cond_dx[i]
            cond_y1 = y + cond_dy[i]
            cond_x2 = x + cond_dx2[i]
            cond_y2 = y + cond_dy2[i]
            nx = x + dx[i]
            ny = y + dy[i]

            if is_valid_pos(cond_x1, cond_y1) and (cond_x1 == r2 and cond_y1 == c2):
                continue
            if is_valid_pos(cond_x2, cond_y2) and (cond_x2 == r2 and cond_y2 == c2):
                continue
            if not is_valid_pos(nx, ny):
                continue
            if visited[nx][ny]:
                continue

            q.append((nx, ny))
            visited[nx][ny] = visited[x][y] + 1
    print(-1)


bfs(r1, c1)
