# https://www.acmicpc.net/problem/1109
# 플래티넘4

import sys
from collections import deque, Counter

input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())
graph = [list(input()) for _ in range(n)]

dx = [1, -1, 0, 0, 1, 1, -1, -1]
dy = [0, 0, 1, -1, 1, -1, 1, -1]

island = {}
visited = [[0] * m for _ in range(n)]


def bfs(x, y, num):
    num += 1
    q = deque([(x, y)])
    visited[x][y] = num
    while q:
        x, y = q.popleft()

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if visited[nx][ny]:
                continue
            if graph[nx][ny] == ".":
                continue
            visited[nx][ny] = num
            q.append((nx, ny))
    return 1


def find_parent(num):
    mini_vis = [[0] * m for _ in range(n)]
    for x in range(n):
        for y in range(m):
            if visited[x][y] != num:
                continue

            mini_vis[x][y] = 1
            q = deque([(x, y)])
            while q:
                x, y = q.popleft()

                if x == 0 or y == 0 or x == n - 1 or y == m - 1:
                    return 0

                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if nx < 0 or ny < 0 or nx >= n or ny >= m:
                        continue
                    if mini_vis[nx][ny]:
                        continue
                    if visited[nx][ny] >= 1:
                        continue
                    q.append((nx, ny))
                    mini_vis[nx][ny] = 1

    for i in range(n):
        for j in range(m):
            if mini_vis[i][j] == 0:
                continue
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if nx < 0 or ny < 0 or nx >= n or ny >= m:
                    continue
                if mini_vis[nx][ny] == 0:
                    return visited[nx][ny]


def calc_height(x=0, i=0):
    if len(T[x]) == 0:
        height[x] = 1
        return
    for next in T[x]:
        calc_height(next, i + 1)
        height[x] = max(height[x], height[next] + 1)


# labeling
cnt = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == ".":
            continue
        if visited[i][j]:
            continue
        cnt += bfs(i, j, cnt)
        island[cnt] = (i, j)

if cnt == 0:
    print(-1)
    exit(0)

# 포함 관계 찾기
parent = [-1] * (cnt + 1)
for i in range(1, cnt + 1):
    parent[i] = find_parent(i)

T = [[] for _ in range(cnt + 1)]
for i, x in enumerate(parent):
    if i == 0:
        continue
    T[x].append(i)

height = [0] * (cnt + 1)


calc_height()
del height[0]

answer = [x[1] for x in sorted(Counter(height).items(), key=lambda x: x[0])]
for x in answer:
    print(x, end=" ")
