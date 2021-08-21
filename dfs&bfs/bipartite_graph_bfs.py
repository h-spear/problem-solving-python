# https://www.acmicpc.net/problem/1707
# 어떠한 그래프 G가 이분 그래프이면 길이가 홀수인 사이클이 존재하지 앟는다.
# 어떠한 그래프 G에 길이가 홀수인 사이클이 존재하지 않는다면 G는 이분 그래프이다.

import sys
from collections import deque

sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

for tc in range(int(input())):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v + 1)]
    visited = [0] * (v + 1)

    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    def bfs():
        q = deque()
        group = 1
        bipartite = True
        for i in range(1, v + 1):
            if visited[i] == 0:
                q.append(i)
                visited[i] = group
                while q:
                    now = q.popleft()
                    for x in graph[now]:
                        if visited[x] == 0:
                            q.append(x)
                            visited[x] = -1 * visited[now]
                        elif visited[x] == visited[now]:
                            bipartite = False
        return bipartite

    print("YES" if bfs() else "NO")
