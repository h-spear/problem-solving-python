# https://www.acmicpc.net/problem/19236

from collections import deque
import numpy

graph = []
fishes = dict()
shark_x, shark_y,shark_dir = 0,0,0


for i in range(4):
  input_data = list(map(int, input().split()))
  row = []
  for j in range(0,8,2):
    row.append((input_data[j],input_data[j+1]))
    fishes[input_data[j]] = (i,j//2)
  graph.append(row)


# 99 : shark
def eating(x,y):
  global shark_x, shark_y, shark_dir
  global fishes
  shark_x, shark_y = x, y
  shark_dir = graph[x][y][1]
  fishes[graph[x][y][0]] = (-1,-1)
  graph[x][y] = (99, shark_dir)

# 1,2,3,4,5,6,7,8
# Up, UL, Left, LD, Down, DR, Right, RU
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

def fishMoving(graph, fishes):
  for j in range(1,len(fishes)):
    x, y = fishes[j]
    if x == y == -1:
      continue
    dir = graph[x][y][1]
    for i in range(8):
      nx = x + dx[(dir + i - 1) % 8]
      ny = y + dy[(dir + i - 1) % 8]
      if nx >= 0 and nx < 4 and ny >= 0 and ny < 4 and graph[nx][ny][0] != 99:
        graph[nx][ny], graph[x][y] = graph[x][y], graph[nx][ny]
        fishes[j], fishes[graph[x][y][0]] = fishes[graph[x][y][0]], fishes[j]
        break


def dfs(x,y):
  if 


while True:
  eating(shark_x,shark_y)