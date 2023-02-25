# https://www.acmicpc.net/problem/9205

import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

for tc in range(int(input())):

    n = int(input())
    graph = []
    for _ in range(n + 2):
        graph.append(tuple(map(int, input().split())))

    def bfs():
        visited = [0] * (n + 2)
        visited[0] = 1
        q = deque([0])
        while q:
            now = q.popleft()

            if now == n + 1:
                return "happy"

            for next in range(1, n + 2):
                if next == now:
                    continue
                if not visited[next] and (
                    abs(graph[next][0] - graph[now][0])
                    + abs(graph[next][1] - graph[now][1])
                    <= 1000
                ):
                    visited[next] = 1
                    q.append(next)
        return "sad"

    print(bfs())
