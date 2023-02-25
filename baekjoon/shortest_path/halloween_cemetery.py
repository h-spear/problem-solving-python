# https://www.acmicpc.net/problem/3860

import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()
INF = float("inf")
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

while 1:
    w, h = map(int, input().split())

    if w == 0 and h == 0:
        break

    g = int(input())
    grave = set()
    hole = {}
    distance = [[INF] * w for _ in range(h)]
    for _ in range(g):
        x, y = map(int, input().split())
        grave.add((y, x))

    e = int(input())
    for _ in range(e):
        x1, y1, x2, y2, t = map(int, input().split())
        hole[(y1, x1)] = (y2, x2, t)

    # spfa
    q = deque()
    q.append((0, 0))
    distance[0][0] = 0
    on = [[0] * w for _ in range(h)]
    on[0][0] = 1
    update = [[0] * w for _ in range(h)]
    cycle = False
    while q:
        x, y = q.popleft()
        on[x][y] = 0

        if x == h - 1 and y == w - 1:
            continue

        if (x, y) in hole:
            nx, ny, t = hole[(x, y)]
            if distance[nx][ny] > distance[x][y] + t:
                distance[nx][ny] = distance[x][y] + t
                if not on[nx][ny]:
                    q.append((nx, ny))
                    on[nx][ny] = 1
                    update[nx][ny] += 1
                    if update[nx][ny] == w * h:
                        cycle = True
                        break
        else:
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or ny < 0 or nx >= h or ny >= w:
                    continue
                if (nx, ny) in grave:
                    continue

                if distance[nx][ny] > distance[x][y] + 1:
                    distance[nx][ny] = distance[x][y] + 1
                    if not on[nx][ny]:
                        q.append((nx, ny))
                        on[nx][ny] = 1
                        update[nx][ny] += 1
                        if update[nx][ny] == w * h:
                            cycle = True
                            break

        if cycle:
            break

    if cycle:
        print("Never")
    elif distance[h - 1][w - 1] == INF:
        print("Impossible")
    else:
        print(distance[h - 1][w - 1])
