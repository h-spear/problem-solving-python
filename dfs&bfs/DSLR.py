# https://www.acmicpc.net/problem/14500


import sys

input = sys.stdin.readline

tetromino = [
    [(0, 1), (1, 0), (1, 1)],
    [(0, 1), (0, 2), (0, 3)],
    [(1, 0), (2, 0), (3, 0)],
    [(1, 0), (1, 1), (2, 1)],
    [(1, 0), (1, -1), (2, -1)],
    [(0, 1), (1, 1), (1, 2)],
    [(0, 1), (-1, 1), (-1, 2)],
    [(0, 1), (0, 2), (1, 2)],
    [(1, 0), (2, 0), (2, -1)],
    [(1, 0), (1, 1), (1, 2)],
    [(0, -1), (1, -1), (2, -1)],
    [(-1, 0), (-1, 1), (-1, 2)],
    [(1, 0), (2, 0), (2, 1)],
    [(0, 1), (0, 2), (-1, 2)],
    [(0, 1), (1, 1), (2, 1)],
    [(0, 1), (-1, 1), (0, 2)],
    [(1, 0), (1, 1), (2, 0)],
    [(0, 1), (1, 1), (0, 2)],
    [(1, 0), (1, -1), (2, 0)],
]

n, m = map(int, input().rstrip().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().rstrip().split())))

answer = 0
for i in range(n):
    for j in range(m):
        for tet in tetromino:
            sum = graph[i][j]
            for dx, dy in tet:
                if i + dx < n and j + dy < m:
                    sum += graph[i + dx][j + dy]
                else:
                    break
                answer = max(answer, sum)

print(answer)
