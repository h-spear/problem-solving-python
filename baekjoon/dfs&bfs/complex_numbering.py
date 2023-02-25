# https://www.acmicpc.net/problem/2667

from collections import deque

n = int(input())
graph = []

for _ in range(n):
    data = list(map(int, list(input())))
    graph.append(data)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

visited = []
total_count = 0
answer = []


def bfs(x, y):
    global total_count
    q = deque([(x, y)])
    visited.append((x, y))
    count = 1

    while q:
        x, y = q.popleft()

        for i in range(4):

            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= 0 and nx < n and ny >= 0 and ny < n and (nx, ny) not in visited:
                if graph[nx][ny] != 0:
                    q.append((nx, ny))
                    visited.append((nx, ny))
                    count += 1
    if count != 0:
        total_count += 1
        return count


for i in range(n):
    for j in range(n):
        if graph[i][j] != 0 and (i, j) not in visited:
            answer.append(bfs(i, j))

answer.sort()

print(total_count)
for x in answer:
    print(x)
