# https://www.acmicpc.net/problem/12893

from collections import defaultdict, deque

n, m = map(int, input().split())
graph = defaultdict(list)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (n + 1)


def bfs(x):
    q = deque([x])
    visited[x] = 1
    while q:
        x = q.popleft()

        for next in graph[x]:
            if visited[next] == visited[x]:
                return False
            if visited[next]:
                continue

            q.append(next)
            visited[next] = -visited[x]
    return True


def solve():
    for i in range(1, n + 1):
        if visited[i] == 0:
            if not bfs(i):
                print(0)
                return
    print(1)


solve()
