# https://www.acmicpc.net/problem/6086


from collections import defaultdict, deque


INF = float("inf")
MAX_V = 52


def c_to_i(alpha):
    if alpha.isupper():
        return ord(alpha) - ord("A")
    else:
        return ord(alpha) - ord("a") + 26


def edmonds_karp(start, end):
    total_flow = 0
    while 1:
        visit = [-1 for _ in range(MAX_V)]
        q = deque([start])

        # bfs
        while q:
            now = q.popleft()
            if now == end:
                break

            for _next in graph[now]:
                if capacity[now][_next] - flow[now][_next] > 0 and visit[_next] == -1:
                    q.append(_next)
                    visit[_next] = now

        if visit[end] == -1:
            break

        min_flow = INF
        i = end
        while i != start:
            min_flow = min(min_flow, capacity[visit[i]][i] - flow[visit[i]][i])
            i = visit[i]

        i = end
        while i != start:
            flow[visit[i]][i] += min_flow
            flow[i][visit[i]] -= min_flow
            i = visit[i]

        total_flow += min_flow

    return total_flow


graph = defaultdict(list)
capacity = [[0] * MAX_V for _ in range(MAX_V)]
flow = [[0] * MAX_V for _ in range(MAX_V)]

n = int(input())
for _ in range(n):
    a, b, c = input().split()
    a = c_to_i(a)
    b = c_to_i(b)
    c = int(c)

    capacity[a][b] += c
    capacity[b][a] += c
    graph[a].append(b)
    graph[b].append(a)

print(edmonds_karp(0, 25))
