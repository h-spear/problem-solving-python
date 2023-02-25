# https://leetcode.com/problems/find-if-path-exists-in-graph/

from collections import deque, defaultdict


class Solution:
    def validPath(
        self, n: int, edges: List[List[int]], source: int, destination: int
    ) -> bool:
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        q = deque([source])
        visited = [False] * (n + 1)
        visited[source] = True
        while q:
            x = q.popleft()

            for y in graph[x]:
                if visited[y]:
                    continue
                q.append(y)
                visited[y] = True

        return visited[destination]
