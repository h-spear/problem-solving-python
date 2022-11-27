# https://www.acmicpc.net/problem/14267

import sys


sys.setrecursionlimit(123456)


def dfs(x, curr):
    answer[x - 1] = curr + node[x]

    for y in graph[x]:
        dfs(y, curr + node[x])


input = lambda: sys.stdin.readline().rstrip()
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
parent = list(map(int, input().split()))
for i, x in enumerate(parent):
    if x == -1:
        continue
    graph[x].append(i + 1)

answer = [0] * n
node = [0] * (n + 1)
for _ in range(m):
    i, w = map(int, input().split())
    node[i] += w

dfs(1, 0)
print(*answer)
