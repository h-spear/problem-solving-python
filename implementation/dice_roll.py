# https://www.acmicpc.net/problem/14499

n, m, x, y, k = map(int, input().split())

graph = []
dice = [0, 0, 0, 0, 0, 0, 0]

# top, up, right
top = 1
up = 2
right = 3

# X 동 서 북 남
dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]

for _ in range(n):
    graph.append(list(map(int, input().split())))

cmd = list(map(int, input().split()))


def roll(direction):
    global top, up, right, x, y

    nx = x + dx[direction]
    ny = y + dy[direction]
    if nx < 0 or nx >= n or ny < 0 or ny >= m:
        return

    x, y = nx, ny
    if direction == 1:
        right, top = top, 7 - right
    elif direction == 2:
        top, right = right, 7 - top
    elif direction == 3:
        up, top = top, 7 - up
    elif direction == 4:
        top, up = up, 7 - top
    # copy

    if graph[x][y] == 0:
        graph[x][y] = dice[7 - top]
    else:
        dice[7 - top] = graph[x][y]
        graph[x][y] = 0
    print(dice[top])


for i in cmd:
    roll(i)
