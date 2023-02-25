# https://leetcode.com/problems/number-of-islands/

from collections import deque


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]

        def bfs(x, y):
            q = deque([(x, y)])
            visited[x][y] = 1
            while q:
                x, y = q.popleft()

                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]

                    if nx < 0 or ny < 0 or nx >= n or ny >= m:
                        continue
                    if visited[nx][ny]:
                        continue
                    if grid[nx][ny] == "0":
                        continue

                    visited[nx][ny] = 1
                    q.append((nx, ny))
            return 1

        n = len(grid)
        m = len(grid[0])
        visited = [[0] * m for _ in range(n)]
        answer = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == "0":
                    continue
                if visited[i][j]:
                    continue
                answer += bfs(i, j)

        return answer
