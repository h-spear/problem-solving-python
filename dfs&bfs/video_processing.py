import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
t = int(input())

processed = []
for x in graph:
    row = []
    for i in range(0, m * 3, 3):
        row.append(1 if (sum(x[i : i + 3]) / 3) >= t else 0)
    processed.append(row)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(x, y):
    q = deque([(x, y)])
    global visited
    visited[x][y] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if visited[x][y]:
                continue
            if graph[x][y] == 0:
                continue

            visited[x][y] = 1
    return 1


visited = [[0] * m for _ in range(n)]
answer = 0
for i in range(n):
    for j in range(m):
        if processed[i][j] == 0:
            continue
        if visited[i][j]:
            continue
        answer += bfs(i, j)

print(answer)
for x in processed:
    print(x)
