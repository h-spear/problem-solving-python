# https://school.programmers.co.kr/learn/courses/15009/lessons/121690

from collections import deque


def solution(n, m, hole):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    hole = set([tuple(h) for h in hole])
    visited = [[[0] * 2 for _ in range(m + 1)] for _ in range(n + 1)]
    visited[1][1][1] = 1
    q = deque([(1, 1, 1)])

    while q:
        x, y, s = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx <= 0 or ny <= 0 or nx > n or ny > m:
                continue
            if (nx, ny) in hole:
                continue
            if visited[nx][ny][s]:
                continue

            q.append((nx, ny, s))
            visited[nx][ny][s] = visited[x][y][s] + 1

        if not s:
            continue

        for i in range(4):
            nx = x + dx[i] * 2
            ny = y + dy[i] * 2

            if nx <= 0 or ny <= 0 or nx > n or ny > m:
                continue
            if (nx, ny) in hole:
                continue
            if visited[nx][ny][0]:
                continue

            q.append((nx, ny, 0))
            visited[nx][ny][0] = visited[x][y][s] + 1

    res1, res2 = visited[n][m]

    if not res1 and not res2:
        return -1
    elif res1:
        return res1 - 1
    elif res2:
        return res2 - 1
    return min(res1, res2) - 1
