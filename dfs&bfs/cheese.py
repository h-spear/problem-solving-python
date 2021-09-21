# https://www.acmicpc.net/problem/2636
# 0(공기)에서 만나는 1(치즈)은 무조건 공기중에 접촉중인 것

import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

m, n = map(int, input().split())
graph = []
for _ in range(m):
    graph.append(list(map(int, input().split())))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs():
    visited = [[False] * n for _ in range(m)]
    q = deque([(0, 0)])
    visited[0][0] = True

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= 0 and nx < m and ny >= 0 and ny < n:
                if visited[nx][ny] == False:
                    visited[nx][ny] = True
                    if graph[nx][ny] == 0:
                        q.append((nx, ny))
                    elif graph[nx][ny] == 1:
                        graph[nx][ny] = 2


def melting():
    cnt = 0
    for i in range(m):
        for j in range(n):
            if graph[i][j] == 2:
                graph[i][j] = 0
                cnt += 1
    return cnt


def haveCheese():
    cnt = 0
    for row in graph:
        cnt += row.count(1)

    if cnt:
        return True
    else:
        return False


answer = 0
last = 0
while haveCheese():
    bfs()
    last = melting()
    answer += 1

print(answer)
print(last)
