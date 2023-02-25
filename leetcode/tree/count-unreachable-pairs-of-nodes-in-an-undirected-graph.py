# https://leetcode.com/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/

from collections import deque


class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        def bfs(x):
            q = deque([x])
            visited[x] = 1
            cnt = 0
            while q:
                x = q.popleft()
                cnt += 1

                for y in graph[x]:
                    if visited[y]:
                        continue
                    q.append(y)
                    visited[y] = 1
            return cnt

        graph = [[] for _ in range(n)]
        visited = [0] * n
        pair = []
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        for i in range(n):
            if visited[i]:
                continue
            pair.append(bfs(i))

        answer = 0
        summation = sum(pair)

        for num in pair:
            summation -= num
            answer += summation * num

        return answer
