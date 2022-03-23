# https://www.acmicpc.net/problem/14500

import sys

input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())
tetromino = [
    [(1, 0), (2, 0), (3, 0)],
    [(0, 1), (0, 2), (0, 3)],
    [(0, 1), (1, 0), (1, 1)],
    [(1, 0), (2, 0), (2, 1)],
    [(0, 1), (-1, 1), (-2, 1)],
    [(-1, 0), (-1, 1), (-1, 2)],
    [(0, 1), (0, 2), (1, 2)],
    [(0, 1), (1, 0), (2, 0)],
    [(0, 1), (1, 1), (2, 1)],
    [(1, 0), (1, 1), (1, 2)],
    [(0, 1), (0, 2), (-1, 2)],
    [(1, 0), (1, 1), (2, 1)],
    [(-1, 0), (-1, 1), (-2, 1)],
    [(0, 1), (1, 1), (1, 2)],
    [(0, 1), (-1, 1), (-1, 2)],
    [(0, 1), (0, 2), (-1, 1)],
    [(0, 1), (0, 2), (1, 1)],
    [(0, 1), (-1, 1), (1, 1)],
    [(1, 0), (2, 0), (1, 1)],
]
graph = [list(map(int, input().split())) for _ in range(n)]
answer = 0
for i in range(n):
    for j in range(m):
        for tet in tetromino:
            temp = graph[i][j]
            for dx, dy in tet:
                if i + dx < 0 or i + dx >= n:
                    break
                if j + dy < 0 or j + dy >= m:
                    break
                temp += graph[i + dx][j + dy]
            answer = max(answer, temp)

print(answer)
