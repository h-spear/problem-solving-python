# https://www.acmicpc.net/problem/17837

n, k = map(int, input().split())
board = []
piece = {}
graph = [[[] for _ in range(n)] for _ in range(n)]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
for _ in range(n):
    board.append(list(map(int, input().split())))

for i in range(k):
    r, c, d = map(int, input().split())
    graph[r - 1][c - 1].append(i)
    piece[i] = (r - 1, c - 1, d - 1)


def rotate_dir(dir):
    if dir <= 1:
        return 1 - dir
    else:
        return 5 - dir


def is_in_area(x, y):
    if x < 0 or y < 0 or x >= n or y >= n:
        return False
    return True


def move_white(p):
    x, y, dir = piece[p]
    nx = x + dx[dir]
    ny = y + dy[dir]

    idx = 0
    for i in range(len(graph[x][y])):
        if graph[x][y][i] == p:
            idx = i
            break

    if is_in_area(nx, ny):
        for i in graph[x][y][idx:]:
            piece[i] = (nx, ny, piece[i][2])

        graph[nx][ny].extend(graph[x][y][idx:])
        graph[x][y] = graph[x][y][:idx]


def move_red(p):
    x, y, dir = piece[p]
    nx = x + dx[dir]
    ny = y + dy[dir]

    idx = 0
    for i in range(len(graph[x][y])):
        if graph[x][y][i] == p:
            idx = i
            break

    if is_in_area(nx, ny):
        for i in graph[x][y][idx:]:
            piece[i] = (nx, ny, piece[i][2])

        for i in range(len(graph[x][y]) - idx):
            graph[nx][ny].append(graph[x][y].pop())


def move_blue(p):
    piece[p] = (piece[p][0], piece[p][1], rotate_dir(piece[p][2]))
    x, y, dir = piece[p]
    nx = x + dx[dir]
    ny = y + dy[dir]

    if is_in_area(nx, ny):
        if board[nx][ny] == 0:
            move_white(p)
        elif board[nx][ny] == 1:
            move_red(p)


def check_state():
    for i in range(n):
        for j in range(n):
            if len(graph[i][j]) >= 4:
                return True
    return False


def move(p):
    x, y, dir = piece[p]
    nx = x + dx[dir]
    ny = y + dy[dir]

    if not is_in_area(nx, ny):
        piece[p] = (piece[p][0], piece[p][1], rotate_dir(piece[p][2]))
        x, y, dir = piece[p]
        nx = x + dx[dir]
        ny = y + dy[dir]

        if board[nx][ny] == 0:
            move_white(p)
        elif board[nx][ny] == 1:
            move_red(p)
    else:
        if board[nx][ny] == 0:
            move_white(p)
        elif board[nx][ny] == 1:
            move_red(p)
        elif board[nx][ny] == 2:
            move_blue(p)


def turn():
    for p in range(k):
        move(p)
        if check_state():
            return True
    return False


def simul():
    for i in range(1, 1001):
        res = turn()

        if res:
            print(i)
            return

    print(-1)
    return


simul()
