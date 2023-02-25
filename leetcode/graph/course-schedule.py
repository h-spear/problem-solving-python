# https://leetcode.com/problems/course-schedule/
# topology sort

from collections import deque, defaultdict


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        in_degree = [0] * numCourses

        for x, y in prerequisites:
            graph[x].append(y)
            in_degree[y] += 1

        q = deque()
        for i in range(numCourses):
            if in_degree[i] == 0:
                q.append(i)

        for i in range(numCourses):
            if not q:
                return False

            x = q.popleft()

            for y in graph[x]:
                in_degree[y] -= 1
                if in_degree[y] == 0:
                    q.append(y)

        return True
