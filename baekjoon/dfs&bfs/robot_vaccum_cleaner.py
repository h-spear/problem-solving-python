# https://www.acmicpc.net/problem/4991
# robovac(로봇청소기)

from collections import deque
from itertools import permutations

INF = float("inf")
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
g_w, g_h = 0, 0
g_graph = []
g_dirty_cnt = 0
g_distance = None
g_mapper_coord_to_num = None


def bfs(x, y):
    q = deque([(x, y)])
    visited = [[0] * g_w for _ in range(g_h)]
    visited[x][y] = 1
    start = g_mapper_coord_to_num[(x, y)]
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= g_h or ny >= g_w:
                continue
            if visited[nx][ny]:
                continue
            if g_graph[nx][ny] == "x":
                continue

            if g_graph[nx][ny] == "*":
                target = g_mapper_coord_to_num[(nx, ny)]
                g_distance[start][target] = visited[x][y]

            visited[nx][ny] = visited[x][y] + 1
            q.append((nx, ny))


def solve(w, h, graph):
    global g_w, g_h, g_distance, g_dirty_cnt, g_mapper_coord_to_num, g_graph, test
    g_w = w
    g_h = h
    g_distance = [[0] * 11 for _ in range(11)]
    g_dirty_cnt = 0
    g_mapper_coord_to_num = dict()
    g_graph = graph
    answer = INF

    for i in range(g_h):
        for j in range(g_w):
            if g_graph[i][j] == "o":
                g_mapper_coord_to_num[(i, j)] = 0
            elif g_graph[i][j] == "*":
                g_dirty_cnt += 1
                g_mapper_coord_to_num[(i, j)] = g_dirty_cnt

    for x, y in g_mapper_coord_to_num:
        bfs(x, y)

    # 방문할 수 없는 dirty 칸이 있으면 바로 -1 리턴
    for i in range(1, g_dirty_cnt + 1):
        if not sum(g_distance[i]):
            return -1

    for candidate in permutations(range(1, g_dirty_cnt + 1), g_dirty_cnt):
        x = 0
        cnt = 0
        for y in candidate:
            cnt += g_distance[x][y]
            x = y
        answer = min(answer, cnt)

    if answer:
        return answer
    else:
        return -1


if __name__ == "__main__":
    while 1:
        w, h = map(int, input().split())

        if w == 0 and h == 0:
            break

        graph = [list(input()) for _ in range(h)]
        print(solve(w, h, graph))
