# https://www.acmicpc.net/problem/2606

v = int(input())
e = int(input())

graph = [[] for _ in range(v + 1)]

for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

result = 0
visited = [False] * (v + 1)


def dfs(x):
    global result
    visited[x] = True

    for c in graph[x]:
        if not visited[c]:
            dfs(c)
            result += 1


dfs(1)
print(result)
