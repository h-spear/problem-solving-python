# https://www.acmicpc.net/problem/21611

import re, sys

input = lambda: sys.stdin.readline().rstrip()
n, m = map(int, input().split())
input_data = [list(input().split()) for _ in range(n)]
command = [list(map(int, input().split())) for _ in range(m)]
graph = []
board = [[0] * n for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
result = [0, 0, 0]

max_length = n * n


def init():
    top, left, bottom, right = 0, 0, n - 1, n - 1
    cnt = n * n - 1
    while top < bottom and left < right:
        for j in range(left, right + 1):
            graph.append(input_data[top][j])
            board[top][j] = cnt
            cnt -= 1
        top += 1

        for i in range(top, bottom + 1):
            graph.append(input_data[i][right])
            board[i][right] = cnt
            cnt -= 1
        right -= 1

        for j in range(right, left - 1, -1):
            graph.append(input_data[bottom][j])
            board[bottom][j] = cnt
            cnt -= 1
        bottom -= 1

        for i in range(bottom, top - 1, -1):
            graph.append(input_data[i][left])
            board[i][left] = cnt
            cnt -= 1
        left += 1
    graph.append("0")
    graph.reverse()


def ice_shards(d, s):
    x, y = n // 2, n // 2
    for i in range(s):
        idx = board[x + dx[d]][y + dy[d]]
        graph[idx] = "0"
        x += dx[d]
        y += dy[d]


def explosion():
    global graph
    changed = True
    temp = "".join(graph)
    temp = re.sub("0", "", temp)

    pattern1 = re.compile("1{4,}")
    pattern2 = re.compile("2{4,}")
    pattern3 = re.compile("3{4,}")
    while changed:
        changed = False

        cnt = len("".join(pattern1.findall(temp)))
        if cnt:
            changed = True
        result[0] += cnt
        temp = pattern1.sub("!", temp)

        cnt = len("".join(pattern2.findall(temp)))
        if cnt:
            changed = True
        result[1] += cnt
        temp = pattern2.sub("!", temp)

        cnt = len("".join(pattern3.findall(temp)))
        if cnt:
            changed = True
        result[2] += cnt
        temp = pattern3.sub("!", temp)

        temp = re.sub("!", "", temp)

    temp = re.sub("111", "#!", temp)
    temp = re.sub("11", "@!", temp)
    temp = re.sub("1", "!!", temp)
    temp = re.sub("222", "#@", temp)
    temp = re.sub("22", "@@", temp)
    temp = re.sub("2", "!@", temp)
    temp = re.sub("333", "##", temp)
    temp = re.sub("33", "@#", temp)
    temp = re.sub("3", "!#", temp)
    temp = re.sub("!", "1", temp)
    temp = re.sub("@", "2", temp)
    temp = re.sub("#", "3", temp)
    graph = ["0"]
    for i in range(min(len(temp), max_length - 1)):
        graph.append(temp[i])

    if len(graph) < max_length:
        graph.extend(["0"] * (max_length - len(graph)))


def blizzard(command):
    init()
    for d, s in command:
        ice_shards(d - 1, s)
        explosion()

    one, two, three = result
    print(one + 2 * two + 3 * three)


blizzard(command)
