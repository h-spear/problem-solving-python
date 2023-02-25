# https://www.acmicpc.net/problem/1738

from collections import defaultdict, deque


n, m = map(int, input().split())
graph = defaultdict(list)
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

INF = float("inf")
distance = [-INF] * (n + 1)
distance[1] = 0
visit = [-1] * (n + 1)


def bfs(x):
    q = deque([x])
    visited = [0] * (n + 1)
    while q:
        x = q.popleft()

        if x == n:
            return True

        for y, _ in graph[x]:
            if visited[y]:
                continue
            q.append(y)
            visited[y] = 1

    return False


def spfa():
    q = deque()
    q.append(1)
    on = [0] * (n + 1)
    on[1] = 1
    update = [0] * (n + 1)

    while q:
        x = q.popleft()
        on[x] = 0

        for y, cost in graph[x]:
            if distance[y] < distance[x] + cost:
                distance[y] = distance[x] + cost
                visit[y] = x
                if not on[y]:
                    q.append(y)
                    on[y] = 1
                    update[y] += 1
                    if update[y] == n:
                        return bfs(y)

    return False


cycle = spfa()

if cycle:
    print(-1)
elif distance[n] == -INF:
    print(-1)
elif visit[1] != -1:
    print(-1)
else:
    stack = []
    i = n
    while i != -1:
        stack.append(i)
        i = visit[i]

    print(*stack[::-1])
