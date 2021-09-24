import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
visited = [[0] * m for _ in range(n)]


def bfs(x, y):
    cnt = 1
    visited[x][y] = 1
    q = deque([(x, y)])
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= 0 and nx < n and ny >= 0 and ny < m:
                if not visited[nx][ny] and graph[nx][ny] == 1:
                    cnt += 1
                    visited[nx][ny] = 1
                    q.append((nx, ny))
    return cnt


cnt = 0
answer = 0
for i in range(n):
    for j in range(m):
        if not visited[i][j] and graph[i][j] == 1:
            cnt += 1
            answer = max(answer, bfs(i, j))

print(cnt)
print(answer)
