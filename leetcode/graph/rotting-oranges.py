# https://leetcode.com/problems/rotting-oranges/

from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        m = len(grid)
        n = len(grid[0])
        visited = [[0] * n for _ in range(m)]
        q = deque()
        answer = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] != 2:
                    continue
                q.append((i, j))
                visited[i][j] = 1

        while q:
            x, y = q.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or ny < 0 or nx >= m or ny >= n:
                    continue
                if visited[nx][ny]:
                    continue
                if grid[nx][ny] != 1:
                    continue
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))

        for i in range(m):
            for j in range(n):
                if grid[i][j] != 1:
                    continue
                if not visited[i][j]:
                    return -1
                if visited[i][j]:
                    answer = max(answer, visited[i][j] - 1)

        return answer
