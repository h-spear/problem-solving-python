# https://leetcode.com/problems/perfect-squares/

from collections import deque


class Solution:
    def numSquares(self, n: int) -> int:

        q = deque([0])
        visited = [0] * (n + 1)
        visited[0] = 1
        while q:
            x = q.popleft()

            for i in range(1, 101):
                nx = x + i * i

                if nx > n:
                    break
                if visited[nx]:
                    continue
                q.append(nx)
                visited[nx] = visited[x] + 1

        return visited[n] - 1
