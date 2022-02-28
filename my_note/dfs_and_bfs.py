from collections import defaultdict, deque


n, m, v = map(int, input().split())
graph = defaultdict(list)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# https://www.acmicpc.net/problem/1260
for i in range(1, n + 1):
    graph[i].sort()


def dfs(x, visited=[0] * (n + 1)):
    visited[x] = 1
    print(x, end=" ")
    for next in graph[x]:
        if visited[next]:
            continue
        dfs(next, visited)


def bfs(x):
    visited = [0] * (n + 1)
    visited[x] = 1
    q = deque([x])
    while q:
        x = q.popleft()
        print(x, end=" ")
        for next in graph[x]:
            if visited[next]:
                continue

            q.append(next)
            visited[next] = 1


dfs(v)
print()

bfs(v)
