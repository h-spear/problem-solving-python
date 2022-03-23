# https://www.acmicpc.net/problem/21608

from collections import OrderedDict

n = int(input())
_dict = OrderedDict()
for _ in range(n ** 2):
    input_data = list(map(int, input().split()))
    key, value = input_data[0], input_data[1:]
    _dict[key] = value

graph = [[0] * n for _ in range(n)]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

answer = 0


def select_pos(num):
    favorite = _dict[num]
    candidate = []
    for x in range(n):
        for y in range(n):
            if graph[x][y] != 0:
                continue

            empty = 0
            favo = 0
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or nx >= n or ny < 0 or ny >= n:
                    continue
                if graph[nx][ny] in favorite:
                    favo += 1
                if graph[nx][ny] == 0:
                    empty += 1

            candidate.append((-favo, -empty, x, y))

    candidate.sort()
    sel_x, sel_y = candidate[0][2], candidate[0][3]
    graph[sel_x][sel_y] = num


def calc_score():
    global answer
    for x in range(n):
        for y in range(n):
            now = graph[x][y]
            favorite = _dict[now]
            favo = 0
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= n or ny < 0 or ny >= n:
                    continue
                if graph[nx][ny] in favorite:
                    favo += 1

            if favo != 0:
                answer += 10 ** (favo - 1)


for key in _dict:
    select_pos(key)
calc_score()
print(answer)
