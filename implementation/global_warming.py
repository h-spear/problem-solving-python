from urllib.parse import MAX_CACHE_SIZE


r, c = map(int, input().split())
graph = [["."] * (c + 2) for _ in range(r + 2)]
for i in range(r):
    row = list(input())
    for j in range(c):
        graph[i + 1][j + 1] = row[j]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def submerged(x, y):
    faced = 0
    for i in range(4):
        if graph[x + dx[i]][y + dy[i]] == ".":
            faced += 1

    return faced >= 3


def show_small_map():
    MAX_WIDTH = c + 2
    MAX_HEIGHT = r + 2
    top, right, bottom, left = 0, 0, 0, 0

    for i in range(MAX_HEIGHT):
        cnt = 0
        for j in range(MAX_WIDTH):
            if graph[i][j] == ".":
                cnt += 1
        if cnt != MAX_WIDTH:
            top = i
            break
    for i in range(MAX_HEIGHT - 1, -1, -1):
        cnt = 0
        for j in range(MAX_WIDTH):
            if graph[i][j] == ".":
                cnt += 1
        if cnt != MAX_WIDTH:
            bottom = i
            break
    for j in range(MAX_WIDTH):
        cnt = 0
        for i in range(MAX_HEIGHT):
            if graph[i][j] == ".":
                cnt += 1
        if cnt != MAX_HEIGHT:
            left = j
            break
    for j in range(MAX_WIDTH - 1, -1, -1):
        cnt = 0
        for i in range(MAX_HEIGHT):
            if graph[i][j] == ".":
                cnt += 1
        if cnt != MAX_HEIGHT:
            right = j
            break

    for i in range(top, bottom + 1):
        for j in range(left, right + 1):
            print(graph[i][j], end="")
        print()


def simulate():
    # 사라질 땅 체크
    checked = [[0] * (c + 2) for _ in range(r + 2)]
    for i in range(1, 1 + r):
        for j in range(1, 1 + c):
            if graph[i][j] == ".":
                continue
            if not submerged(i, j):
                continue
            checked[i][j] = 1

    # 지도에서 지우기
    for i in range(1, 1 + r):
        for j in range(1, 1 + c):
            if checked[i][j] == 0:
                continue
            graph[i][j] = "."

    # 작은 지도로 보여주기
    show_small_map()


simulate()
