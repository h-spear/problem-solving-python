import sys
from collections import deque

n,m = map(int, input().split())
INF = int(1e9)
graph = []
for _ in range(n):
  graph.append(list(map(int, list(sys.stdin.readline().rstrip()))))

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(x,y):
  q = deque([(x,y,1)])
  visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
  visited[x][y][1] = 1

  while q:
    x, y, w = q.popleft()
    if x == n-1 and y == m-1:
      return visited[x][y][w]

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx >=0 and nx < n and ny >= 0 and ny < m:
        if graph[nx][ny] == 1 and w == 1:
          visited[nx][ny][0] = visited[x][y][1] + 1
          q.append((nx,ny,0))
        elif graph[nx][ny] == 0 and visited[nx][ny][w] == 0:
          visited[nx][ny][w] = visited[x][y][w] + 1
          q.append((nx,ny,w))
  return -1

print(bfs(0,0))
