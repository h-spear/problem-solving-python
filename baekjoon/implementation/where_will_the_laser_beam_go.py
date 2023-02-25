# https://www.acmicpc.net/problem/3709

for tc in range(int(input())):
    n, r = map(int, input().split())
    mirror = set()
    visited = [[[0, 0, 0, 0] for _ in range(n + 1)] for _ in range(n + 1)]
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    d = 0
    for _ in range(r):
        x, y = map(int, input().split())
        mirror.add((x, y))

    x, y = map(int, input().split())

    if x == 0:
        d = 2
    elif x == n + 1:
        d = 0
    elif y == 0:
        d = 1
    elif y == n + 1:
        d = 3

    # simulation
    x += dx[d]
    y += dy[d]

    while 1 <= x <= n and 1 <= y <= n:
        if visited[x][y][d] == 1:
            break

        visited[x][y][d] = 1
        if (x, y) in mirror:
            d = (d + 1) % 4

        x += dx[d]
        y += dy[d]

    if 0 not in [x, y] and (n + 1) not in [x, y]:
        print(0, 0)
    else:
        print(x, y)
