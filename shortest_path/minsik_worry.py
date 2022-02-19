# https://www.acmicpc.net/problem/1219

from collections import defaultdict
import sys

input = lambda: sys.stdin.readline().rstrip()
n, s, e, m = map(int, input().split())
INF = float("inf")
edges = []
distance = [INF] * n
graph = defaultdict(list)
for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))
    graph[a].append(b)
money = list(map(int, input().split()))
visited = [0] * n


def dfs(x):
    visited[x] = 1
    if x == e:
        return True

    for next in graph[x]:
        if visited[next]:
            continue
        if dfs(next):
            return True


def bellman_ford(start):
    distance[start] = -money[start]
    for i in range(n):
        for j in range(m):
            now, next, weight = edges[j]
            cost = distance[now] + weight - money[next]

            if distance[now] != -INF and distance[next] > cost:
                distance[next] = cost

                if i == n - 1:
                    # cycle 발생 시 목적지까지 도달 가능해야만 Gee
                    if dfs(next):
                        print("Gee")
                        return

    if distance[e] == INF:
        print("gg")
    else:
        print(-distance[e])


bellman_ford(s)
