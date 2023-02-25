# https://www.acmicpc.net/problem/21609

from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
n, m = map(int, input().split())
graph = []

answer = 0
for i in range(n):
    graph.append(list(map(int, input().split())))


def clear_visited_in_rainbow(visited):
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 0:
                visited[i][j] = 0


def bfs(x, y, visited, color):
    q = deque([(x, y)])
    visited[x][y] = 1
    cnt = 1
    cnt_rainbow = 0
    group = [(x, y)]
    r, c = x, y
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if visited[nx][ny]:
                continue
            if graph[nx][ny] <= -1:
                continue
            if graph[nx][ny] >= 1:
                if graph[nx][ny] != color:
                    continue

                if r > nx:
                    r, c = nx, ny
                elif r == nx:
                    if c > ny:
                        r, c = nx, ny
            if graph[nx][ny] == 0:
                cnt_rainbow += 1
            q.append((nx, ny))
            group.append((nx, ny))
            visited[nx][ny] = 1
            cnt += 1

    if cnt <= 1:
        return None
    else:
        return [-cnt, -cnt_rainbow, -r, -c, group]


def find_largest_blockgroup():
    visited = [[0] * n for _ in range(n)]
    groups = []
    for i in range(n):
        for j in range(n):
            if graph[i][j] <= 0:
                continue
            if visited[i][j]:
                continue
            res = bfs(i, j, visited, graph[i][j])
            if res:
                groups.append(res)
            clear_visited_in_rainbow(visited)

    groups.sort()
    if not groups:
        return 0, []

    cnt, _, _, _, group = groups[0]
    return -cnt, group


def remove_blockgroup(group):
    for x, y in group:
        graph[x][y] = -2


def gravity(graph):
    for i in range(n - 2, -1, -1):
        for j in range(n):
            if graph[i][j] <= -1:
                continue

            nx = i
            while nx != n - 1 and graph[nx + 1][j] == -2:
                nx += 1
            graph[i][j], graph[nx][j] = graph[nx][j], graph[i][j]


def rotate_matrix_270(A):
    n = len(A)  # length of row
    m = len(A[0])  # length of column
    result = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[m - j - 1][i] = A[i][j]
    return result


def simulation():
    global answer, graph
    while 1:
        cnt, largest_group = find_largest_blockgroup()
        if cnt == 0:
            break
        answer += cnt ** 2
        remove_blockgroup(largest_group)
        gravity(graph)
        graph = rotate_matrix_270(graph)
        gravity(graph)

    print(answer)


simulation()
