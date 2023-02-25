# https://leetcode.com/problems/shortest-path-visiting-all-nodes/


class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        def dfs(x, vis, depth):
            if (x, vis) in visited and visited[(x, vis)] <= depth:
                return
            if depth >= answer[0]:
                return
            if vis == all_visited:
                answer[0] = min(answer[0], depth)
                return

            visited[(x, vis)] = depth
            for y in graph[x]:
                dfs(y, vis | 1 << y, depth + 1)

        visited = {}
        n = len(graph)
        all_visited = 2 ** n - 1
        answer = [123456789]

        for i in range(n):
            dfs(i, 1 << i, 0)

        return answer[0]
