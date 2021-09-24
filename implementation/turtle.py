# https://www.acmicpc.net/problem/8911

INF = int(1e9)
for tc in range(int(input())):
    cmd = input()

    # 북, 동, 남, 서
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    dir = 0

    visited = {(0, 0)}
    x, y = 0, 0
    i = 0
    while i < len(cmd):
        c = cmd[i]
        if c == "F":
            x += dx[dir]
            y += dy[dir]
            visited.add((x, y))
        elif c == "B":
            x -= dx[dir]
            y -= dy[dir]
            visited.add((x, y))
        elif c == "L":
            dir = (dir + 3) % 4
        elif c == "R":
            dir = (dir + 1) % 4
        i += 1

    x_max, x_min, y_max, y_min = -INF, INF, -INF, INF
    for x, y in visited:
        x_max = max(x_max, x)
        x_min = min(x_min, x)
        y_max = max(y_max, y)
        y_min = min(y_min, y)

    print(abs(x_max - x_min) * abs(y_max - y_min))
