# https://www.acmicpc.net/problem/14503

import sys

input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())
r, c, dir = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

# top, right, down, left
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

count = 1
visited = [[False] * m for _ in range(n)]
visited[r][c] = True

# simulation
while True:
    clean = False
    for i in range(4):
        dir = (dir + 3) % 4
        nr = r + dr[dir]
        nc = c + dc[dir]
        if graph[nr][nc] == 0 and visited[nr][nc] == False:
            visited[nr][nc] = True
            r, c = nr, nc
            count += 1
            clean = True
            break

    if not clean:
        nr = r + dr[(dir + 2) % 4]
        nc = c + dc[(dir + 2) % 4]
        if graph[nr][nc] == 1:
            break
        else:
            r, c = nr, nc

print(count)
