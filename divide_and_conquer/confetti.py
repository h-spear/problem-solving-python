# https://www.acmicpc.net/problem/2630

import sys, copy
input = sys.stdin.readline

n = int(input().rstrip())
paper = []
for _ in range(n):
  paper.append(list(map(int, input().rstrip().split())))

def check(graph):
  white = 0
  blue = 0
  for i in range(len(graph)):
    for j in range(len(graph)):
      if graph[i][j] == 1:
        blue += 1
      else:
        white += 1

  if white >= 0 and blue == 0:
    return 0  # 하얀 종이
  elif blue >= 0 and white == 0:
    return 1  # 파란 종이
  else:
    return -1 # mixed

def divide(graph):
  length = len(graph)
  graph_1 = [[0] * (length//2) for _ in range(length//2)]
  graph_2 = copy.deepcopy(graph_1)
  graph_3 = copy.deepcopy(graph_1)
  graph_4 = copy.deepcopy(graph_1)
  
  for i in range(length//2):
    for j in range(length//2):
      graph_1[i][j] = graph[i][j]
      graph_2[i][j] = graph[i][j+length//2]
      graph_3[i][j] = graph[i+length//2][j]
      graph_4[i][j] = graph[i+length//2][j+length//2]
  
  return graph_1,graph_2,graph_3,graph_4

def solution(graph):
  global blue, white
  divided = divide(graph)
  for paper in divided:
    p = check(paper) 
    if p == 1:
      blue += 1
    elif p == 0:
      white += 1 
    else:
      solution(paper)

def handle(graph):
  global blue, white
  p = check(graph) 
  if p == 1:
    blue += 1
  elif p == 0:
    white += 1 
  else:
    solution(graph)

blue = 0
white = 0
handle(paper)
print(white)
print(blue)