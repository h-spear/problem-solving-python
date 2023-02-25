# https://www.acmicpc.net/problem/1260

from collections import deque

n, m, start = map(int, input().split())

graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


for i in range(n + 1):
    graph[i].sort()

result_dfs = []
result_bfs = []


def dfs(x):
    visited[x] = True
    result_dfs.append(x)

    for node in graph[x]:
        if not visited[node]:
            dfs(node)


def bfs(x):
    visited = [False] * (n + 1)
    q = deque([x])
    visited[x] = True
    result_bfs.append(x)

    while q:
        now = q.popleft()

        for node in graph[now]:

            if not visited[node]:
                q.append(node)
                visited[node] = True
                result_bfs.append(node)


def print_array(arr):
    for x in arr:
        print(x, end=" ")
    print()


dfs(start)
bfs(start)
print_array(result_dfs)
print_array(result_bfs)
