# https://www.acmicpc.net/problem/18405

from collections import deque

n, k = map(int, input().split())

graph = []
virus = []

for i in range(n):
    input_data = list(map(int, input().split()))
    graph.append(input_data)
    for j in range(n):
        if input_data[j] != 0:
            virus.append((input_data[j], 0, i, j))

# 정렬 후 큐로
virus.sort()
q = deque(virus)

s, x, y = map(int, input().split())

# up left down right
dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]

while q:
    v, sec, r, c = q.popleft()

    if s == sec:
        break

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if nr >= 0 and nr < n and nc >= 0 and nc < n:
            if graph[nr][nc] == 0:
                graph[nr][nc] = v
                q.append((v, sec + 1, nr, nc))

print(graph[x - 1][y - 1])
