# https://programmers.co.kr/learn/courses/30/lessons/49189
# 코딩테스트 고득점 Kit : graph


from collections import deque


def bfs(graph, n):
    q = deque([1])
    visited = [0] * (n + 1)
    visited[1] = 1
    farthest = -1
    while q:
        x = q.popleft()

        for next in graph[x]:
            if visited[next]:
                continue
            visited[next] = visited[x] + 1
            q.append(next)
            farthest = max(farthest, visited[next])
    return visited.count(farthest)


def solution(n, edge):
    graph = [[] for _ in range(n + 1)]
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
    return bfs(graph, n)
