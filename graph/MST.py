# https://www.acmicpc.net/problem/1197
# Minimum Spanning Tree

import sys

def find(parent, x):
  if parent[x] != x:
    parent[x] = find(parent, parent[x])
  return parent[x]

def union(parent, a, b):
  a = find(parent, a)
  b = find(parent, b)

  if a < b:
    parent[b] = a
  else:
    parent[a] = b

v, e = map(int, input().split())

edges = []
for _ in range(e):
  a, b, c = map(int, sys.stdin.readline().rstrip().split())
  edges.append((c,a,b))
edges.sort()

parent = [0] * (v+1)
for i in range(1,v+1):
  parent[i] = i

# kruskal
result = 0
for edge in edges:
  c, a, b = edge

  if find(parent, a) != find(parent, b):
    result += c
    union(parent,a,b)

print(result)
