# https://leetcode.com/problems/number-of-islands/

from collections import deque


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        answer = 0
        n, m = len(grid), len(grid[0])

        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]

        def bfs(x, y):
            q = deque([(x, y)])
            grid[x][y] = "0"
            while q:
                x, y = q.popleft()

                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]

                    if nx < 0 or ny < 0 or nx >= n or ny >= m:
                        continue
                    if grid[nx][ny] == "0":
                        continue
                    q.append((nx, ny))
                    grid[nx][ny] = "0"

        for i in range(n):
            for j in range(m):
                if grid[i][j] == "0":
                    continue
                bfs(i, j)
                answer += 1

        return answer
