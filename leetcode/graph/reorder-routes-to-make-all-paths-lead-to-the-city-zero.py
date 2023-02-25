# https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/

from collections import defaultdict, deque


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(list)
        for a, b in connections:
            graph[a].append((b, 1))
            graph[b].append((a, 0))

        q = deque([0])
        visited = [0] * n
        visited[0] = 1
        answer = 0
        while q:
            x = q.popleft()

            for y, cost in graph[x]:
                if visited[y]:
                    continue

                answer += cost
                visited[y] = 1
                q.append(y)

        return answer
