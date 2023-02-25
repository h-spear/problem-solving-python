# https://www.acmicpc.net/problem/23288


from collections import deque

n, m, k = map(int, input().split())
graph = []
dice = {"up": 2, "down": 5, "left": 4, "right": 3, "top": 1, "bottom": 6}
dir = 0
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
pos_x, pos_y = 0, 0
score = 0
for _ in range(n):
    graph.append(list(map(int, input().split())))


def dice_rotate():
    if dir == 0:
        dice["top"], dice["right"], dice["bottom"], dice["left"] = (
            dice["left"],
            dice["top"],
            dice["right"],
            dice["bottom"],
        )
    elif dir == 1:
        dice["up"], dice["top"], dice["down"], dice["bottom"] = (
            dice["bottom"],
            dice["up"],
            dice["top"],
            dice["down"],
        )
    elif dir == 2:
        dice["top"], dice["right"], dice["bottom"], dice["left"] = (
            dice["right"],
            dice["bottom"],
            dice["left"],
            dice["top"],
        )
    else:
        dice["up"], dice["top"], dice["down"], dice["bottom"] = (
            dice["top"],
            dice["down"],
            dice["bottom"],
            dice["up"],
        )


def dice_roll():
    global pos_x, pos_y, dir
    nx = pos_x + dx[dir]
    ny = pos_y + dy[dir]
    if nx < 0 or ny < 0 or nx >= n or ny >= m:
        dir = (dir + 2) % 4
        dice_roll()
        return

    pos_x = nx
    pos_y = ny
    dice_rotate()


def bfs(num):
    q = deque([(pos_x, pos_y)])
    visited = [[0] * m for _ in range(n)]
    visited[pos_x][pos_y] = 1
    cnt = 1
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if visited[nx][ny]:
                continue
            if graph[nx][ny] != num:
                continue
            visited[nx][ny] = 1
            q.append((nx, ny))
            cnt += 1
    return cnt


def get_score():
    num = graph[pos_x][pos_y]
    cnt = bfs(num)
    return num * cnt


def change_dir():
    global dir
    num = graph[pos_x][pos_y]
    if num < dice["bottom"]:
        dir = (dir + 1) % 4
    elif num > dice["bottom"]:
        dir = (dir - 1) % 4
    else:
        pass


def simulation():
    global score
    for _ in range(k):
        dice_roll()
        score += get_score()
        change_dir()

    print(score)


simulation()
