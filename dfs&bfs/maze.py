from collections import deque

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

visited = [[0] * m for _ in range(n)]


# up down left right
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def bfs(r, c):
    queue = deque()
    queue.append((r, c))
    visited[r][c] = 1
    while queue:
        v = queue.popleft()
        for d in direction:
            nr = v[0] + d[0]
            nc = v[1] + d[1]
            if nr >= 0 and nr < n and nc >= 0 and nc < m:
                if visited[nr][nc] == 0 and graph[nr][nc] == 1:
                    visited[nr][nc] = visited[v[0]][v[1]] + 1
                    queue.append((nr, nc))

    return visited[n - 1][m - 1]


print(bfs(0, 0))
