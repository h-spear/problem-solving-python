# https://leetcode.com/problems/network-delay-time/

from collections import defaultdict
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        INF = float('inf')
        graph = defaultdict(list)
        
        for a,b,d in times:
            graph[a].append((b,d))
            
        distance = [INF] * (n + 1)
        def dijkstra(k):
            heap = [(0,k)]
            distance[k] = 0
            while heap:
                dist, now = heapq.heappop(heap)
                
                if dist > distance[now]:
                    continue
                
                for v, w in graph[now]:
                    cost = dist + w
                    if cost < distance[v]:
                        heapq.heappush(heap, (cost, v))
                        distance[v] = cost
                        
        dijkstra(k)
        return -1 if distance[1:].count(INF) else max(distance[1:])
