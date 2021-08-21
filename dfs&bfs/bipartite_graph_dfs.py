# https://www.acmicpc.net/problem/1707
# 어떠한 그래프 G가 이분 그래프이면 길이가 홀수인 사이클이 존재하지 앟는다.
# 어떠한 그래프 G에 길이가 홀수인 사이클이 존재하지 않는다면 G는 이분 그래프이다.

import sys

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

    def dfs(x, group):
        visited[x] = group
        for i in graph[x]:
            if visited[i] == 0:  # 가보지 않은 노드이면 방문
                if not dfs(i, -group):
                    return False
            elif visited[i] == visited[x]:  # 그룹이 동일하면 False
                return False
        return True

    bipartite = True
    for i in range(1, v + 1):
        if visited[i] == 0:
            bipartite = dfs(i, 1)
            if not bipartite:
                break

    print("YES" if bipartite else "NO")
