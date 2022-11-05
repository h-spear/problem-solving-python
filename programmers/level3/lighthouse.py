# https://school.programmers.co.kr/learn/courses/30/lessons/133500

from collections import defaultdict
import sys

sys.setrecursionlimit(10 ** 6)

visited = None
graph = None


def dfs(x):
    visited[x] = 1
    if len(graph[x]) == 1 and visited[graph[x][0]] == 1:
        visited[x] = -1
        return

    for y in graph[x]:
        if visited[y]:
            continue
        dfs(y)

    for y in graph[x]:
        if visited[y] == -1:

            visited[x] = 1
            return
    visited[x] = -1


def solution(n, lighthouse):
    global graph, visited
    if n == 2:
        return 1

    graph = defaultdict(list)
    visited = [0] * (n + 1)

    for x, y in lighthouse:
        graph[x].append(y)
        graph[y].append(x)

    dfs(1)
    return visited.count(1)
