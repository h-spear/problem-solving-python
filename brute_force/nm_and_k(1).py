# https://www.acmicpc.net/problem/18290

import sys

input = lambda: sys.stdin.readline().rstrip()
n, m, k = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
visited = [[0] * m for _ in range(n)]
answer = -123456


def func(x, y, sum, depth):
    global answer

    if depth == k:
        answer = max(answer, sum)
        return

    for i in range(x, n):
        for j in range(y if i == x else 0, m):
            if visited[i][j]:
                continue

            flag = False
            for l in range(4):
                nx = i + dx[l]
                ny = j + dy[l]

                if nx < 0 or ny < 0 or nx >= n or ny >= m:
                    continue
                if visited[nx][ny]:
                    flag = True
                    break

            if flag:
                continue

            visited[i][j] = 1
            func(i, j, sum + graph[i][j], depth + 1)
            visited[i][j] = 0


func(0, 0, 0, 0)
print(answer)
