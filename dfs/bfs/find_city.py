# https://www.acmicpc.net/problem/18352

from collections import deque

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
  start, end = map(int, input().split())
  graph[start].append(end)

distance = [-1] * (n+1)
q = deque([x])
distance[x] = 0

while q:
  now = q.popleft()
  for i in graph[now]:
    if distance[i] == -1:
      distance[i] = distance[now] + 1
      q.append(i)

if distance.count(k) == 0:
  print(-1)
else:
  for i in range(n+1):
    if distance[i] == k:
      print(i)