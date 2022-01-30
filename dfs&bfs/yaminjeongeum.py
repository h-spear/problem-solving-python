from collections import deque

a, b = map(int, input().split())
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)


def bfs(x, y):
    q = deque([(x, 0)])
    visited = [0] * (n + 1)
    visited[x] = 1
    while q:
        now, t = q.popleft()

        if now == y:
            return t

        for x in graph[now]:
            if visited[x]:
                continue
            q.append((x, t + 1))
            visited[x] = 1
    return -1


print(bfs(a, b))
