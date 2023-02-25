# https://leetcode.com/problems/time-needed-to-inform-all-employees/

from collections import defaultdict


class Solution:
    def numOfMinutes(
        self, n: int, headID: int, manager: List[int], informTime: List[int]
    ) -> int:
        graph = defaultdict(list)
        for y, x in enumerate(manager):
            if x == -1:
                continue
            graph[x].append(y)

        visited = [-1] * n
        visited[headID] = 0
        q = deque()
        q.append(headID)
        while q:
            x = q.popleft()

            for y in graph[x]:
                if visited[y] == 0:
                    continue
                visited[y] = visited[x] + informTime[x]
                q.append(y)

        return max(visited)
