# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=4&contestProbId=AV14vXUqAGMCFAYD&categoryId=AV14vXUqAGMCFAYD&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=ALL&select-1=4&pageSize=10&pageIndex=1

# import sys
# sys.stdin = open("input.txt", "r")

from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    tc = int(input())
    graph = []
    for _ in range(16):
        graph.append(list(map(int, list(input()))))

    sx, sy = 0, 0
    tx, ty = 0, 0

    for i in range(16):
        for j in range(16):
            if graph[i][j] == 2:
                sx, sy = i, j
            elif graph[i][j] == 3:
                tx, ty = i, j

    # bfs
    visited = [[0] * 16 for _ in range(16)]
    visited[sx][sy] = 1
    q = deque([(sx, sy)])
    result = 0

    while q:
        x, y = q.popleft()
        if x == tx and y == ty:
            result = 1
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= 16 or ny >= 16:
                continue
            if visited[nx][ny]:
                continue
            if graph[nx][ny] == 1:
                continue
            q.append((nx, ny))
            visited[nx][ny] = 1

    print(f"#{tc} {result}")

    # ///////////////////////////////////////////////////////////////////////////////////
