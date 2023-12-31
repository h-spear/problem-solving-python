# https://www.acmicpc.net/problem/16985

from collections import deque

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

answer = float("inf")


def bfs(graph):
    global answer
    for x, y, z in [
        (0, 0, 0),
        (0, 0, 4),
        (0, 4, 0),
        (0, 4, 4),
        (4, 0, 0),
        (4, 0, 4),
        (4, 4, 0),
        (4, 4, 4),
    ]:
        if graph[x][y][z] == 0:
            continue
        target_x, target_y, target_z = 4 - x, 4 - y, 4 - z
        q = deque([(x, y, z)])
        visited = [[[0] * 5 for _ in range(5)] for _ in range(5)]
        visited[x][y][z] = 1
        while q:
            x, y, z = q.popleft()

            if x == target_x and y == target_y and z == target_z:
                answer = min(answer, visited[x][y][z] - 1)
                return

            for i in range(6):
                nx = x + dx[i]
                ny = y + dy[i]
                nz = z + dz[i]

                if nx < 0 or ny < 0 or nz < 0 or nx >= 5 or ny >= 5 or nz >= 5:
                    continue
                if visited[nx][ny][nz]:
                    continue
                if graph[nx][ny][nz] == 0:
                    continue

                q.append((nx, ny, nz))
                visited[nx][ny][nz] = visited[x][y][z] + 1


def rotate_matrix_90(A):
    n = len(A)  # length of row
    m = len(A[0])  # length of column
    result = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[j][n - i - 1] = A[i][j]
    return result


def dfs(depth=0):
    global three_dim_graph, used

    if depth == 5:
        bfs(three_dim_graph)
        return

    for layer in range(5):
        for i in range(4):
            if depth == 0 and i >= 1:
                continue
            if layer in used:
                continue
            used.append(layer)
            three_dim_graph[depth] = graph[layer][i]
            dfs(depth + 1)
            used.pop()


graph = [[] for _ in range(5)]
for i in range(5):
    graph[i].append([list(map(int, input().split())) for _ in range(5)])
    for r in range(3):
        graph[i].append(rotate_matrix_90(graph[i][r]))
three_dim_graph = [None] * 5
used = []

dfs()
print(-1 if answer == float("inf") else answer)
