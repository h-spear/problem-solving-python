# https://leetcode.com/problems/as-far-from-land-as-possible/

from collections import deque


class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        q = deque()
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    q.append((i, j))
        visited = [[0] * n for _ in range(n)]

        while q:
            x, y = q.popleft()

            for i in range(4):
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

        answer = 0
        for row in visited:
            answer = max(answer, max(row))

        if answer:
            return answer
        return -1
