# https://www.acmicpc.net/problem/3055

from collections import deque
import copy

n, m = map(int, input().split())
graph = []
for _ in range(n):
  graph.append(list(input()))

x, y = 0, 0 
target_x, target_y = 0,0
for i in range(n):
  for j in range(m):
    if graph[i][j] == 'S':
      x, y = i, j
    if graph[i][j] == 'D':
      target_x,target_y = i,j
    

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def watering():
  global graph
  graph_copy = copy.deepcopy(graph)
  for x in range(n):
    for y in range(m):
      if graph[x][y] == '*':
        for i in range(4):
          nx = x + dx[i]
          ny = y + dy[i]
          if nx >= 0 and nx < n and ny>=0 and ny<m:
            if graph[nx][ny] != 'D' and graph[nx][ny] != 'X':
              graph_copy[nx][ny] = '*'
  graph = graph_copy

visited = [[-1] * m for _ in range(n)]

def bfs(x,y):
  q = deque([(x,y)])
  visited[x][y] = 0
  
  while q:
    qlen = len(q)
    watering()
    while qlen:
      x, y = q.popleft()
      if x == target_x and y== target_y:
        return visited[target_x][target_y]

      for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= 0 and nx < n and ny >=0 and ny<m:
          if graph[nx][ny] != 'X' and graph[nx][ny] != '*' and visited[nx][ny] == -1:
            visited[nx][ny] = visited[x][y] + 1
            q.append((nx,ny))
      qlen -= 1

  return 'KAKTUS'

print(bfs(x,y))
