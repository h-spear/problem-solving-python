# https://leetcode.com/problems/is-graph-bipartite/


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        def bfs(x):
            q = deque([x])
            visited[x] = 1
            while q:
                x = q.popleft()

                for y in graph[x]:
                    if visited[y]:
                        if visited[y] == visited[x]:
                            return False
                    else:
                        visited[y] = -visited[x]
                        q.append(y)

            return True

        n = len(graph)
        visited = [0] * n

        for i in range(n):
            if visited[i]:
                continue
            if not bfs(i):
                return False

        return True
