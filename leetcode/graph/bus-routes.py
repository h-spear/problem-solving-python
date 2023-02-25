# https://leetcode.com/problems/bus-routes/

from collections import deque, defaultdict


class Solution:
    def numBusesToDestination(
        self, routes: List[List[int]], source: int, target: int
    ) -> int:
        if source == target:
            return 0

        n = len(routes)
        graph = defaultdict(list)
        for i in range(n):
            routes[i] = set(routes[i])
            for x in routes[i]:
                graph[x].append(i)

        q = deque()
        visited = [0] * n
        for src in graph[source]:
            q.append(src)
            visited[src] = 1

        while q:
            i = q.popleft()

            if target in routes[i]:
                return visited[i]

            for x in routes[i]:
                for dst in graph[x]:
                    if visited[dst]:
                        continue
                    q.append(dst)
                    visited[dst] = visited[i] + 1

        return -1
