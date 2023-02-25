# https://leetcode.com/problems/max-area-of-island/

from collections import deque


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]

        def bfs(x, y):
            q = deque([(x, y)])
            visited[x][y] = 1
            area = 1
            while q:
                x, y = q.popleft()

                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]

                    if nx < 0 or ny < 0 or nx >= n or ny >= m:
                        continue
                    if visited[nx][ny]:
                        continue
                    if not grid[nx][ny]:
                        continue

                    visited[nx][ny] = 1
                    q.append((nx, ny))
                    area += 1
            return area

        n = len(grid)
        m = len(grid[0])
        visited = [[0] * m for _ in range(n)]
        answer = 0

        for i in range(n):
            for j in range(m):
                if visited[i][j]:
                    continue
                if not grid[i][j]:
                    continue
                answer = max(answer, bfs(i, j))

        return answer
