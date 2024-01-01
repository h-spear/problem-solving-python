# https://www.acmicpc.net/problem/1525

from collections import deque


def change(graph, x1, y1, x2, y2):
    graph[x1][y1], graph[x2][y2] = graph[x2][y2], graph[x1][y1]


def hashing(graph):
    _hash = ""
    for i in range(3):
        for j in range(3):
            _hash += graph[i][j]
    return _hash


def find_zero(graph):
    for x in range(3):
        for y in range(3):
            if graph[x][y] == "0":
                return (x, y)
    return None


def get_candidates(status):
    graph = [[status[i * 3 + j] for j in range(3)] for i in range(3)]

    x, y = find_zero(graph)
    candidates = []
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or ny < 0 or nx >= 3 or ny >= 3:
            continue

        change(graph, x, y, nx, ny)
        candidates.append(hashing(graph))
        change(graph, x, y, nx, ny)

    return candidates


def bfs(start):
    visited = set()
    visited.add(start)
    q = deque()
    q.append(start)
    cnt = 0
    while q:
        for _ in range(len(q)):
            now = q.popleft()

            if now == target:
                return cnt

            for nxt in get_candidates(now):
                if nxt in visited:
                    continue
                q.append(nxt)
                visited.add(nxt)

        cnt += 1

    return -1


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
target = "123456780"

if __name__ == "__main__":
    status = ""
    for _ in range(3):
        status += input().replace(" ", "")

    print(bfs(status))
