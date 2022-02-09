# https://leetcode.com/problems/course-schedule/
# 방향 그래프의 cycle 구하는 법
# 무방향 그래프는 union-find로 구현할 수 있음


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]

        for a, b in prerequisites:
            graph[a].append(b)

        traced = set()
        visited = [0] * numCourses

        def dfs(i):
            if i in traced:
                return False
            if visited[i]:
                return True

            traced.add(i)
            for y in graph[i]:
                if not dfs(y):
                    return False
            traced.remove(i)
            visited[i] = 1

            return True

        for x in range(numCourses):
            if not dfs(x):
                return False

        return True
