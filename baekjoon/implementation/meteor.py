# https://www.acmicpc.net/problem/10703

from typing import *

r: int
s: int
graph: List[List[str]]
results: List[List[str]]

r, s = map(int, input().split())
graph = [list(input()) for _ in range(r)]

i: int
j: int

# find fallen height
fallHeight: int = 12345

for j in range(s):
    gndRow: int = -1
    for i in range(r - 1, -1, -1):
        if graph[i][j] == "#":
            gndRow = i
        elif graph[i][j] == "X":
            fallHeight = min(fallHeight, gndRow - i - 1)
            break

# move
results = [[(char if char != "X" else ".") for char in line] for line in graph]

for j in range(s):
    for i in range(r - 1, -1, -1):
        if graph[i][j] == "X":
            results[i + fallHeight][j] = graph[i][j]

for i in range(r):
    print("".join(results[i]))
