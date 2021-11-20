# https://www.acmicpc.net/problem/2660
from collections import deque

n = int(input())
graph = [[] for _ in range(51)]
while 1:
    a, b = map(int, input().split())
    if a == b == -1:
        break
    graph[a].append(b)
    graph[b].append(a)


def bfs(x):
    visited = [0] * 51
    visited[x] = 1
    q = deque([x])
    while q:
        now = q.popleft()
        for x in graph[now]:
            if visited[x] != 0:
                continue
            visited[x] = visited[now] + 1
            q.append(x)
    return max(visited) - 1


min_score, num = int(1e9), 0
candidates = []
for i in range(1, n + 1):
    score = bfs(i)
    if score > min_score:
        continue
    elif score < min_score:
        min_score = score
        candidates = [i]
        num = 1
    else:
        candidates.append(i)
        num += 1

print(min_score, num)
for x in sorted(candidates):
    print(x, end=" ")
