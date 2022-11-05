# https://blog.goorm.io/hyundaimobis_preliminary/4/
# 2022 현대모비스 알고리즘 경진대회 예선 문제 3

import heapq


def get_danger_score(x, y):
    if graph[x][y] in ["E", "S"]:
        return 0

    score = 0
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or ny < 0 or nx >= w or ny >= h:
            continue
        if graph[nx][ny] == "P":
            score += 1

    if graph[x][y] == "P":
        score -= 3
    return score


graph = []
sx, sy = 0, 0
ex, ey = 0, 0
dx = [-1, 0, 1, 0, -1, -1, 1, 1]
dy = [0, -1, 0, 1, -1, 1, -1, 1]
answer = 0
w, h = map(int, input().split())

for _ in range(w):
    graph.append(list(input()))

for i in range(w):
    for j in range(h):
        if graph[i][j] == "0":
            graph[i][j] = "z"
        elif graph[i][j] == "S":
            sx, sy = i, j
        elif graph[i][j] == "E":
            ex, ey = i, j

heap = []
heapq.heappush(heap, (0, sx, sy))
visited = [[0] * h for _ in range(w)]

while heap:
    prio, x, y = heapq.heappop(heap)

    if x == ex and y == ey:
        break
    if visited[x][y]:
        continue
    visited[x][y] = 1
    answer += get_danger_score(x, y)

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= w or ny >= h:
            continue
        if visited[nx][ny]:
            continue

        heapq.heappush(heap, (graph[nx][ny], nx, ny))

print(max(answer, 0))
