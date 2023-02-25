# https://www.acmicpc.net/problem/4396


def count_land_mine(n, graph, x, y):
    cnt = 0
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            continue
        if graph[nx][ny] == "*":
            cnt += 1
    return str(cnt)


n = int(input())
graph = [input() for _ in range(n)]
dx = [1, -1, 0, 0, 1, 1, -1, -1]
dy = [0, 0, 1, -1, 1, -1, 1, -1]
selected = [list(input()) for _ in range(n)]
fail = False
for i in range(n):
    for j in range(n):
        if selected[i][j] == ".":
            continue
        if graph[i][j] == "*":
            fail = True
        selected[i][j] = count_land_mine(n, graph, i, j)

if fail:
    for i in range(n):
        for j in range(n):
            if graph[i][j] == "*":
                selected[i][j] = "*"

for row in selected:
    print("".join(row))
