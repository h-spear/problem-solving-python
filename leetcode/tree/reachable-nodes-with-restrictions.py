# https://leetcode.com/problems/reachable-nodes-with-restrictions/

from collections import defaultdict, deque


class Solution:
    def reachableNodes(
        self, n: int, edges: List[List[int]], restricted: List[int]
    ) -> int:
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        restricted = set(restricted)
        visited = [0] * (n + 1)
        q = deque([0])
        answer = 0
        visited[0] = 1
        while q:
            x = q.popleft()
            answer += 1
            for y in graph[x]:
                if visited[y]:
                    continue
                if y in restricted:
                    continue
                q.append(y)
                visited[y] = 1

        return answer
