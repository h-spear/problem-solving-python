# https://www.acmicpc.net/problem/16956

import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

r, c = map(int, input().split())
graph = [list(input()) for _ in range(r)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def fence_installation():
    for x in range(r):
        for y in range(c):
            if graph[x][y] != "S":
                continue

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or ny < 0 or nx >= r or ny >= c:
                    continue
                if graph[nx][ny] == ".":
                    graph[nx][ny] = "D"
                if graph[nx][ny] == "W":
                    return 0
    return 1


is_possible = fence_installation()
print(is_possible)
if is_possible:
    for x in graph:
        print("".join(x))
