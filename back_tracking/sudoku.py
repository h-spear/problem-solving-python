# https://www.acmicpc.net/problem/2580

graph = []
empty = []
for _ in range(9):
    graph.append(list(map(int, input().split())))

for i in range(9):
    for j in range(9):
        if graph[i][j] == 0:
            empty.append((i, j))

le = len(empty)


def check_vertical(x, y, num):
    for i in range(9):
        if i == x:
            continue
        if graph[i][y] == num:
            return False
    return True


def check_horizontal(x, y, num):
    for j in range(9):
        if j == y:
            continue
        if graph[x][j] == num:
            return False
    return True


def check_squere(x, y, num):
    _x = (x // 3) * 3
    _y = (y // 3) * 3
    for i in range(_x, _x + 3):
        for j in range(_y, _y + 3):
            if i == x and j == y:
                continue
            if graph[i][j] == num:
                return False
    return True


def dfs(i):
    if i == le:
        for r in graph:
            print(*r)
        exit(0)

    x, y = empty[i]
    for e in range(1, 10):
        if not check_horizontal(x, y, e):
            continue
        if not check_vertical(x, y, e):
            continue
        if not check_squere(x, y, e):
            continue

        graph[x][y] = e
        dfs(i + 1)
        graph[x][y] = 0


dfs(0)
