# https://leetcode.com/problems/number-of-closed-islands/

from collections import deque


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        visited = [[0] * m for _ in range(n)]
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]

        def bfs(x, y):
            flag = True
            q = deque([(x, y)])
            visited[x][y] = 1
            while q:
                x, y = q.popleft()

                if x == 0 or x == n - 1 or y == 0 or y == m - 1:
                    flag = False

                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]

                    if nx < 0 or ny < 0 or nx >= n or ny >= m:
                        continue
                    if visited[nx][ny]:
                        continue
                    if grid[nx][ny] == 1:
                        continue

                    visited[nx][ny] = 1
                    q.append((nx, ny))

            return flag

        answer = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    continue
                if visited[i][j]:
                    continue

                if bfs(i, j):
                    answer += 1

        return answer
