# https://www.acmicpc.net/problem/11724

from collections import deque
import sys

n, m =  map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
  a, b = map(int, sys.stdin.readline().rstrip().split())
  graph[a].append(b)
  graph[b].append(a)

def bfs(x):
  if visited[x] == True:
    return None

  q = deque([x])
  visited[x] = True
  while q:
    now = q.popleft()
    
    for x in graph[now]:
      if visited[x] == False:
        q.append(x)
        visited[x] = True

  return True

answer = 0
for i in range(1,n+1):
  if bfs(i):
    answer+=1

print(answer)