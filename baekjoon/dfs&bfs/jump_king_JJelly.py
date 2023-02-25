# https://www.acmicpc.net/problem/16174

from collections import deque

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]


def bfs():
    q = deque([(0, 0)])
    visited = [[0] * n for _ in range(n)]
    visited[0][0] = 1
    while q:
        x, y = q.popleft()
        jump = graph[x][y]

        if graph[x][y] == -1:
            print("HaruHaru")
            return

        for i in range(2):
            nx = x + i * jump
            ny = y + (1 - i) * jump

            if nx >= n or ny >= n:
                continue
            if visited[nx][ny]:
                continue

            q.append((nx, ny))
            visited[nx][ny] = 1

    print("Hing")


bfs()
