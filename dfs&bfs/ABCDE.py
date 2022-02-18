# https://www.acmicpc.net/problem/13023

from collections import defaultdict

n, m = map(int, input().split())
graph = defaultdict(list)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * n
answer = 0


def dfs(i, depth=1):
    global answer
    if depth == 5:
        answer = 1
        return

    for next in graph[i]:
        if visited[next]:
            continue
        visited[next] = 1
        dfs(next, depth + 1)
        visited[next] = 0


for i in range(n):
    if not answer:
        visited[i] = 1
        dfs(i)
        visited[i] = 0

print(answer)
