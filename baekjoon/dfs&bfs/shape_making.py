# https://www.acmicpc.net/problem/16932

import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(x, y, num):
    global visited
    q = deque([(x, y)])
    visited[x][y] = num
    cnt = 1
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if visited[nx][ny]:
                continue
            if graph[nx][ny] == 0:
                continue

            q.append((nx, ny))
            visited[nx][ny] = num
            cnt += 1
    return cnt


visited = [[0] * m for _ in range(n)]
size = [0]
cnt = 1

# 모양 나누기
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            continue
        if visited[i][j]:
            continue
        size.append(bfs(i, j, cnt))
        cnt += 1

answer = 0
for i in range(n):
    for j in range(m):
        if visited[i][j]:
            continue

        contact = set()
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if visited[nx][ny]:
                contact.add(visited[nx][ny])

        sum = 0
        for x in list(contact):
            sum += size[x]
        answer = max(answer, sum + 1)

print(answer)
