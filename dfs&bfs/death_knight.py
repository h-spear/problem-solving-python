# https://www.acmicpc.net/problem/16948

from collections import deque

n = int(input())
r1, c1, r2, c2 = map(int, input().split())

dx = [-2, -2, 0, 0, 2, 2]
dy = [-1, 1, -2, 2, -1, 1]

q = deque([(r1, c1)])
visited = [[-1] * n for _ in range(n)]
visited[r1][c1] = 0

while q:
    x, y = q.popleft()

    if x == r2 and y == c2:
        print(visited[x][y])
        exit()

    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= 0 and nx < n and ny >= 0 and ny < n:
            if visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))

print(-1)
