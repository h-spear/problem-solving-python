# https://www.acmicpc.net/problem/2578

graph = []
moderator = []
for _ in range(5):
    graph.append(list(map(int, input().split())))

for _ in range(5):
    moderator.extend(list(map(int, input().split())))


def check_bingo():
    cnt = 0
    for i in range(5):
        is_bingo = True
        for j in range(5):
            if graph[i][j] != 0:
                is_bingo = False
                break
        if is_bingo:
            cnt += 1

    for i in range(5):
        is_bingo = True
        for j in range(5):
            if graph[j][i] != 0:
                is_bingo = False
                break
        if is_bingo:
            cnt += 1

    is_bingo = True
    for i in range(5):
        if graph[i][i] != 0:
            is_bingo = False
    if is_bingo:
        cnt += 1

    is_bingo = True
    for i in range(5):
        if graph[i][4 - i] != 0:
            is_bingo = False
    if is_bingo:
        cnt += 1

    if cnt >= 3:
        return True


def find_num(num):
    for i in range(5):
        for j in range(5):
            if graph[i][j] == num:
                return i, j


for idx, num in enumerate(moderator):
    x, y = find_num(num)
    graph[x][y] = 0
    if check_bingo():
        print(idx + 1)
        break
