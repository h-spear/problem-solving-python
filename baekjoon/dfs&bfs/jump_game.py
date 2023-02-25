# https://www.acmicpc.net/problem/15558

from collections import deque

n, k = map(int, input().split())
graph = [list(map(int, list(input()))) for _ in range(2)]

# 0:left, 1:right
def bfs():
    q = deque([(0, 0, 0)])
    visited = [[0] * n for _ in range(2)]
    visited[0][0] = 1
    while q:
        side, x, time = q.popleft()
        if x + k >= n:
            return 1
        if not visited[side][x + 1] and graph[side][x + 1] == 1:
            visited[side][x + 1] = 1
            q.append((side, x + 1, time + 1))
        if x - 1 > time and not visited[side][x - 1] and graph[side][x - 1] == 1:
            visited[side][x - 1] = 1
            q.append((side, x - 1, time + 1))
        if not visited[1 - side][x + k] and graph[1 - side][x + k] == 1:
            visited[1 - side][x + k] = 1
            q.append((1 - side, x + k, time + 1))
    return 0


print(bfs())
