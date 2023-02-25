# https://www.acmicpc.net/problem/1939
# binary search + graph

from collections import deque


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
s, e = map(int, input().split())


def bfs(w):
    visited = [0] * (n + 1)
    visited[s] = 1
    q = deque([s])

    while q:
        x = q.popleft()

        if x == e:
            return True

        for next, dist in graph[x]:
            if visited[next]:
                continue
            if dist < w:
                continue

            visited[next] = 1
            q.append(next)

    return False


left = 1
right = 1000000000
answer = 0
while left <= right:
    mid = (left + right) // 2

    if bfs(mid):
        left = mid + 1
        answer = mid
    else:
        right = mid - 1


print(answer)
