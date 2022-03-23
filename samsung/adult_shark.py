# https://www.acmicpc.net/problem/19237
# 종료조건이 헷갈려서 시간을 많이 잡아먹힘.
# 1,000회 포함해야 함

import sys
from copy import deepcopy

input = lambda: sys.stdin.readline().rstrip()
n, m, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
direction = list(map(int, input().split()))
shark_infos = dict()
odor = [[(0, 0)] * n for _ in range(n)]
priority = dict()

for num in range(1, m + 1):
    temp = []
    for _ in range(4):
        input_data = list(map(int, input().split()))
        for i in range(4):
            input_data[i] -= 1
        temp.append(input_data)

    priority[num] = temp


def initialization():
    for i in range(n):
        for j in range(n):
            num = graph[i][j]
            if num == 0:
                continue
            shark_infos[num] = (i, j, direction[num - 1] - 1)
            graph[i][j] = num
            odor[i][j] = (num, k + 1)


def get_next_position(num):
    x, y, dir = shark_infos[num]
    temp = []
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            continue

        cond1 = 0 if odor[nx][ny][0] == 0 else 1
        cond2 = 0 if odor[nx][ny][0] == num else 1
        cond3 = priority[num][dir].index(i)

        temp.append((cond1, cond2, cond3, nx, ny, i))
    temp.sort()
    _, _, _, nx, ny, nd = temp[0]
    return nx, ny, nd


def reduce_odor():
    for i in range(n):
        for j in range(n):
            num, sm = odor[i][j]
            if sm == 0:
                continue
            if sm - 1 == 0:
                odor[i][j] = (0, 0)
            else:
                odor[i][j] = (num, sm - 1)


def shark_move():
    global graph, odor
    reduce_odor()
    graph = [[0] * n for _ in range(n)]
    temp = deepcopy(odor)
    for num in range(1, m + 1):
        x, y, d = shark_infos[num]
        if x == -1 and y == -1 and d == -1:
            continue

        nx, ny, nd = get_next_position(num)
        if not graph[nx][ny] or graph[nx][ny] > num:
            shark_infos[num] = (nx, ny, nd)
            graph[nx][ny] = num
            temp[nx][ny] = (num, k + 1)
        else:
            shark_infos[num] = (-1, -1, -1)

    odor = temp


def satisfy_condition():
    for num in range(2, m + 1):
        x, y, d = shark_infos[num]
        if x != -1 or y != -1 or d != -1:
            return False
    return True


def simulation():
    initialization()

    cnt = 0
    while not satisfy_condition():
        cnt += 1
        shark_move()
        if cnt == 1001:
            break

    print(-1 if cnt == 1001 else cnt)


simulation()
