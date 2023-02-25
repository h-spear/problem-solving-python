# https://leetcode.com/problems/all-paths-from-source-to-target/


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        paths = []
        path = [0]

        def back_tracking(x):
            if x == n - 1:
                paths.append(path.copy())
                return

            for y in graph[x]:
                path.append(y)
                back_tracking(y)
                path.pop()

        back_tracking(0)
        return paths
