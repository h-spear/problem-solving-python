import sys
from itertools import combinations
import copy

n, m = map(int, input().split())
labor = []
virus = []
wall = []
empty = []

for i in range(n):
  input_data = list(map(int, sys.stdin.readline().rstrip().split()))
  labor.append(input_data)
  for j in range(m):
    if input_data[j] == 0:
      empty.append((i,j))
    elif input_data[j] == 1:
      wall.append((i,j))
    else:
      virus.append((i,j))

def buildWall(labor_copied, selected):
  for i,j in selected:
    labor_copied[i][j] = 1
  return labor_copied
  
def infection(labor, virus_pos):
  r = virus_pos[0]
  c = virus_pos[1]
  labor[r][c] = 2

  if r-1 >= 0 and labor[r-1][c] == 0:
    infection(labor, (r-1,c))
  if r+1 < n and labor[r+1][c] == 0:
    infection(labor, (r+1,c))
  if c-1 >= 0 and labor[r][c-1] == 0:
    infection(labor, (r,c-1))
  if c+1 < m and labor[r][c+1] == 0:
    infection(labor, (r,c+1))

def virus_test(labor):
  for X in virus:
    infection(labor, X)

def countSafetyZone(labor):
  count = 0 
  for row in labor:
    count += row.count(0)
  return count

# simulation
answer = -1
for case in combinations(empty,3):
  labor_to_simulation = buildWall(copy.deepcopy(labor), case)
  virus_test(labor_to_simulation)
  answer = max(answer, countSafetyZone(labor_to_simulation))

print(answer)