# https://www.acmicpc.net/problem/10993

import re

n = int(input())
c = 1
r = 1

lhs = [1]
lvs = [1]
for _ in range(n - 1):
    c = 2 * c + 3
    r = 2 * r + 1
    lhs.append(c)
    lvs.append(r)

graph = [[" "] * c for _ in range(r)]


def func(n, x, y, lv, lh):
    if n == 1:
        graph[x][y] = "*"
        return

    if n & 1:
        for j in range(y, y + lh):
            graph[x + lv - 1][j] = "*"
        for i in range(x, x + lv):
            graph[2 * x + lv - i - 1][y + i - x] = "*"
            graph[2 * x + lv - i - 1][y + lh - i + x - 1] = "*"
        func(
            n - 1, x + lvs[n - 2], y + lh // 2 - lhs[n - 2] // 2, lvs[n - 2], lhs[n - 2]
        )
    else:
        for j in range(y, y + lh):
            graph[x][j] = "*"
        for i in range(x + 1, x + lv):
            graph[i][y + i - x] = "*"
            graph[i][y + lh - i + x - 1] = "*"
        func(n - 1, x + 1, y + lh // 2 - lhs[n - 2] // 2, lvs[n - 2], lhs[n - 2])


func(n, 0, 0, r, c)
pattern = re.compile(" *$")
for row in graph:
    temp = "".join(row)
    print(pattern.sub("", temp))
