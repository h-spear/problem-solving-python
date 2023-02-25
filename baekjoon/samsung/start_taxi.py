# https://www.acmicpc.net/problem/19238
# 발견하기 쉽지 않았던 예외사항 : 목적지에 도달할 수 없는 승객이 하나라도 있는 경우
# possible_dest_all 변수로 만약 한 명이라도 도달할 수 없는 경우가 있다면 simulation할 필요없이 바로 -1.

import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()
n, m, fuel = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
stx, sty = map(int, input().split())
stx -= 1
sty -= 1
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
passengers = {}
possible_dest_all = True

for _ in range(m):
    px, py, tx, ty = map(int, input().split())
    passengers[(px - 1, py - 1)] = [tx - 1, ty - 1]


def bfs(px, py):
    global possible_dest_all
    q = deque([(px, py)])
    visited = [[0] * n for _ in range(n)]
    visited[px][py] = 1
    tx, ty = passengers[(px, py)]
    while q:
        x, y = q.popleft()

        if x == tx and y == ty:
            passengers[(px, py)].append(visited[x][y] - 1)
            return

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if visited[nx][ny]:
                continue
            if graph[nx][ny] == 1:
                continue
            visited[nx][ny] = visited[x][y] + 1
            q.append((nx, ny))
    possible_dest_all = False


def find_next_passenger(stx, sty):
    q = deque([(stx, sty)])
    visited = [[0] * n for _ in range(n)]
    visited[stx][sty] = 1
    candidates = []

    if (stx, sty) in passengers:
        return stx, sty, 0

    while q:
        x, y = q.popleft()

        if (x, y) in passengers:
            if candidates:
                if candidates[-1][2] < visited[x][y] - 1:
                    break
            candidates.append((x, y, visited[x][y] - 1))

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if visited[nx][ny]:
                continue
            if graph[nx][ny] == 1:
                continue
            visited[nx][ny] = visited[x][y] + 1
            q.append((nx, ny))

    candidates.sort()
    if not candidates:
        return None
    x, y, cost = candidates[0]
    return x, y, cost


def simulation():
    global stx, sty, fuel
    for x, y in passengers:
        bfs(x, y)

    if not possible_dest_all:
        print(-1)
        return

    while passengers:
        res = find_next_passenger(stx, sty)
        if not res:
            print(-1)
            return
        x, y, cost_to_passenger = res
        tx, ty, cost_to_destination = passengers[(x, y)]
        if cost_to_passenger + cost_to_destination > fuel:
            print(-1)
            return

        fuel -= cost_to_passenger
        fuel -= cost_to_destination
        stx = tx
        sty = ty
        del passengers[(x, y)]
        fuel += 2 * cost_to_destination
    print(fuel)


simulation()
