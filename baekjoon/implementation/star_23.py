# https://www.acmicpc.net/problem/13015

import re

n = int(input())
r = 2 * n - 1
c = r + 2 * (n - 1)

graph = [[" "] * c for _ in range(r)]
for i in range(1, r // 2 + 1):
    for j in [0, n - 1]:
        graph[i][i + j] = "*"
        graph[i][c - i - j - 1] = "*"
        graph[r - i - 1][i + j] = "*"
        graph[r - i - 1][c - i - j - 1] = "*"

pattern = re.compile(" *$")
print("*" * n + " " * (c - 2 * n) + "*" * n, sep="")
for i in range(1, r - 1):
    temp = "".join(graph[i])
    print(pattern.sub("", temp))
print("*" * n + " " * (c - 2 * n) + "*" * n, sep="")
