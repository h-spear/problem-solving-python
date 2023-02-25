# https://leetcode.com/problems/possible-bipartition/

from collections import deque, defaultdict


class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
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

        visited = [0] * (n + 1)
        graph = defaultdict(list)
        for a, b in dislikes:
            graph[a].append(b)
            graph[b].append(a)

        for i in range(1, n + 1):
            if not visited[i]:
                if not bfs(i):
                    return False
        return True
