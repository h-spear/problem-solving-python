# https://leetcode.com/problems/course-schedule-ii/

from collections import deque, defaultdict


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        in_degree = [0] * numCourses

        for a, b in prerequisites:
            graph[b].append(a)
            in_degree[a] += 1

        # topology sort
        result = []
        q = deque()

        for i in range(numCourses):
            if in_degree[i] == 0:
                q.append(i)

        for i in range(numCourses):
            if not q:
                return []

            x = q.popleft()
            result.append(x)

            for y in graph[x]:
                in_degree[y] -= 1
                if in_degree[y] == 0:
                    q.append(y)

        return result
