# https://www.acmicpc.net/problem/17822

import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()
n, m, t = map(int, input().split())
graph = []
cmd = []
for _ in range(n):
    graph.append(deque(map(int, input().split())))

for _ in range(t):
    cmd.append(list(map(int, input().split())))


def rotate_disc(i, d, k):
    if d == 0:
        for _ in range(k):
            x = graph[i].pop()
            graph[i].appendleft(x)
    else:
        for _ in range(k):
            x = graph[i].popleft()
            graph[i].append(x)


def remove():
    removed = set()
    for i in range(n):
        for j in range(-1, m - 1):
            if graph[i][j] != 0 and graph[i][j] == graph[i][j + 1]:
                removed.add((i, j))
                removed.add((i, j + 1))

    for j in range(m):
        for i in range(n - 1):
            if graph[i][j] != 0 and graph[i][j] == graph[i + 1][j]:
                removed.add((i, j))
                removed.add((i + 1, j))

    for i, j in removed:
        graph[i][j] = 0

    return len(removed) != 0


def calc_total():
    total_sum = 0
    cnt = 0
    for i in range(n):
        total_sum += sum(graph[i])
        cnt += m - graph[i].count(0)
    return total_sum, cnt


def operation_avg():
    total_sum, cnt = calc_total()
    average = 0
    if cnt != 0:
        average = total_sum / cnt

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                continue
            if graph[i][j] > average:
                graph[i][j] -= 1
            elif graph[i][j] < average:
                graph[i][j] += 1


def command(x, d, k):
    nx = x
    while nx <= n:
        rotate_disc(nx - 1, d, k)
        nx += x

    res = remove()
    if not res:
        operation_avg()


for x, d, k in cmd:
    command(x, d, k)

print(calc_total()[0])
