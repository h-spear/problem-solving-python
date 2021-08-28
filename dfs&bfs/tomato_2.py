# https://www.acmicpc.net/problem/7569

import sys
from collections import deque
input = sys.stdin.readline

m,n,h = map(int, input().rstrip().split())
graph = []
for _ in range(h):
  inner = []
  for _ in range(n):
    inner.append(list(map(int, input().rstrip().split())))
  graph.append(inner)


dx = [0,0,0,0,1,-1]
dy = [1,-1,0,0,0,0]
dz = [0,0,1,-1,0,0]

visited = [[[-1] * m for _ in range(n)] for _ in range(h)]
def bfs():
  q = deque()
  for i in range(h):
    for j in range(n):
      for k in range(m):
        if graph[i][j][k] == 1:
          q.append((i,j,k))
          visited[i][j][k] = 0
          
  while q:
    x,y,z = q.popleft()

    for i in range(6):
      nx = x + dx[i]
      ny = y + dy[i]
      nz = z + dz[i]

      if nx >= 0 and nx < h and ny >= 0 and ny < n and nz >= 0 and nz < m:
        if graph[nx][ny][nz] == 0 and visited[nx][ny][nz] == -1:
          graph[nx][ny][nz] = 1
          visited[nx][ny][nz] = visited[x][y][z] + 1
          q.append((nx,ny,nz))

bfs()

success = True
result= -1
for i in range(h):
  for j in range(n):
    for k in range(m):
      if graph[i][j][k] == 0 and visited[i][j][k] == -1:
        success = False
        break
      result = max(result, visited[i][j][k])
print(result if success else -1)
