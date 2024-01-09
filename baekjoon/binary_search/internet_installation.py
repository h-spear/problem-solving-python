# https://www.acmicpc.net/problem/1800

import sys
import heapq

input = lambda: sys.stdin.readline().rstrip()
INF = float("inf")
N = -1
K = -1
graph = None


def test(most_expensive):
    distance = [INF] * (N + 1)
    distance[1] = 0
    heap = []
    heapq.heappush(heap, (0, 1))

    while heap:
        dist, now = heapq.heappop(heap)

        if distance[now] < dist:
            continue

        for next, d in graph[now]:
            cost = dist + (1 if d > most_expensive else 0)
            if distance[next] > cost:
                distance[next] = cost
                heapq.heappush(heap, (cost, next))

    return distance[N] <= K


def main():
    global N, K, graph

    N, P, K = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    for _ in range(P):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        graph[b].append((a, c))

    # binary search
    left = 0
    right = 1_000_000
    answer = -1
    while left <= right:
        mid = (left + right) >> 1
        if test(mid):
            right = mid - 1
            answer = mid
        else:
            left = mid + 1

    print(answer)


if __name__ == "__main__":
    main()
