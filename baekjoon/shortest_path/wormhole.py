# https://www.acmicpc.net/problem/1865
# https://www.acmicpc.net/board/view/72995

import sys

input = lambda: sys.stdin.readline().rstrip()

for tc in range(int(input())):
    n, m, w = map(int, input().split())
    edges = []
    # INF 를 float('inf')로 하면 오답
    INF = 2000000000
    for _ in range(m):
        s, e, t = map(int, input().split())
        edges.append((s, e, t))
        edges.append((e, s, t))

    for _ in range(w):
        s, e, t = map(int, input().split())
        edges.append((s, e, -t))

    def bellman_ford(start):
        distance = [INF] * (n + 1)
        distance[start] = 0
        for i in range(n):
            for j in range(len(edges)):
                now, next, cost = edges[j]
                if distance[next] > distance[now] + cost:
                    distance[next] = distance[now] + cost

                    if i == n - 1:
                        return True
        return False

    possible = bellman_ford(1)
    print("YES" if possible else "NO")

# 시간 초과
for tc in range(int(input())):
    n, m, w = map(int, input().split())
    edges = []
    INF = 2000000000
    for _ in range(m):
        s, e, t = map(int, input().split())
        edges.append((s, e, t))
        edges.append((e, s, t))

    for _ in range(w):
        s, e, t = map(int, input().split())
        edges.append((s, e, -t))

    def bellman_ford(start):
        distance = [INF] * (n + 1)
        distance[start] = 0
        for i in range(n):
            for j in range(len(edges)):
                now, next, cost = edges[j]
                if distance[now] != INF and distance[next] > distance[now] + cost:
                    distance[next] = distance[now] + cost

                    if i == n - 1:
                        return True
        return False

    possible = False
    for i in range(1, n + 1):
        if possible:
            break
        possible = bellman_ford(i)
    print("YES" if possible else "NO")
