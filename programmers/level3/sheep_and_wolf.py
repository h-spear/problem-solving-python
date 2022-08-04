# https://school.programmers.co.kr/learn/courses/30/lessons/92343
# 참고 : https://blog.encrypted.gg/1029
# bit로 그래프 방문 상태 체크

from collections import defaultdict

g_info = None
graph = defaultdict(list)
visited = [0] * (1 << 17)
n = 0
answer = 0


def search(vis):
    global answer

    if visited[vis]:
        return

    visited[vis] = 1
    wolf = 0
    sheep = 0
    for i in range(n):
        if not vis & (1 << i):
            continue

        if g_info[i] == 1:
            wolf += 1
        else:
            sheep += 1

    if wolf >= sheep:
        return
    answer = max(answer, sheep)

    for i in range(n):
        if not vis & (1 << i):
            continue
        for _next in graph[i]:
            search(vis | (1 << _next))


def solution(info, edges):
    global graph, g_info, n, answer
    n = len(info)
    g_info = info

    for a, b in edges:
        graph[a].append(b)

    search(1)
    return answer
