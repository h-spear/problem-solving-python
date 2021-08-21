# https://www.acmicpc.net/problem/2644

from collections import deque

n = int(input())
x, target = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n + 1)


def bfs(x, target):
    q = deque([(0, x)])
    visited[x] = True

    while q:
        cost, x = q.popleft()
        if x == target:
            print(cost)
            return

        for i in graph[x]:
            if not visited[i]:
                visited[i] = True
                q.append((cost + 1, i))
    print(-1)
    return


bfs(x, target)
