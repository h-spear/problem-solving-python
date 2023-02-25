# https://www.acmicpc.net/problem/11657
# SPFA(Shortest Path Faster Algorithm)
# Edge relaxation
# 음수 가중치 간선을 가진 그래프에서도 사용 가능
# SPFA Time Complexity : average O(E), worst O(VE)
# Bellman Ford Time Complexity : O(VE)

from collections import defaultdict, deque


def spfa(start):
    q = deque()
    q.append(start)
    on = [0] * (n + 1)
    on[start] = 1
    distance[start] = 0
    update = [0] * (n + 1)
    while q:
        x = q.popleft()
        on[x] = 0

        for y, cost in graph[x]:
            if distance[y] > distance[x] + cost:
                distance[y] = distance[x] + cost
                if not on[y]:
                    on[y] = 1
                    update[y] += 1
                    q.append(y)

                    # 어떠한 노드가 update가 n번 일어났다면
                    # 해당 노드를 포함하는 음의 사이클이 존재
                    if update[y] == n:
                        print(-1)
                        return

    for i in range(2, n + 1):
        if distance[i] == INF:
            print(-1)
        else:
            print(distance[i])


n, m = map(int, input().split())
graph = defaultdict(list)
edges = []
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

INF = float("inf")
distance = [INF] * (n + 1)


spfa(1)
