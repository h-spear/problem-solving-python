# https://leetcode.com/problems/shortest-path-with-alternating-colors/

import heapq
from collections import defaultdict


class Solution:
    def shortestAlternatingPaths(
        self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]
    ) -> List[int]:
        def dijkstra(start_color):
            distance[start_color][0] = 0
            heap = []
            heapq.heappush(heap, (0, start_color, 0))
            while heap:
                dist, color, x = heapq.heappop(heap)

                if dist > distance[color][x]:
                    continue

                for y in graph[color][x]:
                    cost = dist + 1
                    if distance[1 - color][y] > cost:
                        distance[1 - color][y] = cost
                        heapq.heappush(heap, (cost, 1 - color, y))

        INF = float("inf")
        graph = [defaultdict(list), defaultdict(list)]
        answer = []

        for a, b in redEdges:
            graph[0][a].append(b)
        for u, v in blueEdges:
            graph[1][u].append(v)

        distance = [[INF] * n for _ in range(2)]

        dijkstra(0)
        dijkstra(1)

        for i in range(n):
            dist = min(distance[0][i], distance[1][i])
            if dist == INF:
                answer.append(-1)
            else:
                answer.append(dist)

        return answer
