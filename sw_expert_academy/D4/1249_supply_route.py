# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=4&contestProbId=AV15QRX6APsCFAYD&categoryId=AV15QRX6APsCFAYD&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=ALL&select-1=4&pageSize=10&pageIndex=1

# import sys
# sys.stdin = open("input.txt", "r")

import heapq

INF = float("inf")
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def dijkstra(graph, n):
    distance = [[INF] * n for _ in range(n)]
    distance[0][0] = 0
    heap = []
    heapq.heappush(heap, (0, 0, 0))
    while heap:
        dist, x, y = heapq.heappop(heap)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if distance[nx][ny] <= dist + graph[nx][ny]:
                continue
            distance[nx][ny] = dist + graph[nx][ny]
            heapq.heappush(heap, (dist + graph[nx][ny], nx, ny))

    return distance[n - 1][n - 1]


T = int(input())
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    n = int(input())
    graph = []
    for _ in range(n):
        graph.append(list(map(int, list(input()))))

    print(f"#{test_case} {dijkstra(graph, n)}")

    # ///////////////////////////////////////////////////////////////////////////////////
