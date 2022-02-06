# https://programmers.co.kr/learn/courses/30/lessons/43162
# 코딩테스트 고득점 Kit : dfs/bfs


def dfs(graph, now, visited):
    visited[now] = 1
    for i, x in enumerate(graph[now]):
        if x == 0:
            continue
        if visited[i]:
            continue
        dfs(graph, i, visited)
    return 1


def solution(n, computers):
    visited = [0] * n
    answer = 0
    for i in range(n):
        if visited[i]:
            continue
        answer += dfs(computers, i, visited)
    return answer
