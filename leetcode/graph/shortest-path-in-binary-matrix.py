# https://leetcode.com/problems/shortest-path-in-binary-matrix/

from collections import deque


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1

        dx = [1, -1, 0, 0, 1, 1, -1, -1]
        dy = [0, 0, 1, -1, 1, -1, 1, -1]
        n = len(grid)
        visited = [[0] * n for _ in range(n)]
        visited[0][0] = 1
        q = deque([(0, 0)])

        while q:
            x, y = q.popleft()

            if x == n - 1 and y == n - 1:
                return visited[x][y]

            for i in range(8):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or ny < 0 or nx >= n or ny >= n:
                    continue
                if grid[nx][ny]:
                    continue
                if visited[nx][ny]:
                    continue

                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))

        return -1
