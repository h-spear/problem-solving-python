# https://www.acmicpc.net/problem/10990

import re

n = int(input())
c = 2 * n - 1
r = n
graph = [[" "] * c for _ in range(r)]

graph[0][c // 2] = "*"
for i in range(1, r):
    graph[i][c // 2 - i] = "*"
    graph[i][c // 2 + i] = "*"

pattern = re.compile(" +$")

for row in graph:
    string = "".join(row)
    print(pattern.sub("", string))
