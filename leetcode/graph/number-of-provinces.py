# https://leetcode.com/problems/number-of-provinces/

from collections import deque


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def bfs(x):
            q = deque([x])
            visited[x] = 1
            while q:
                x = q.popleft()

                for i in range(node_count):
                    if visited[i + 1]:
                        continue
                    if isConnected[x - 1][i] == 1:
                        q.append(i + 1)
                        visited[i + 1] = 1
            return 1

        node_count = len(isConnected)
        visited = [0] * (node_count + 1)
        answer = 0

        for i in range(1, node_count + 1):
            if visited[i]:
                continue
            answer += bfs(i)

        return answer
