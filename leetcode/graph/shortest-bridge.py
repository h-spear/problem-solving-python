# https://leetcode.com/problems/shortest-bridge/

from collections import deque


class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        def bfs(x, y):
            visited[x][y] = 1
            q = deque([(x, y)])
            land = [(x, y)]
            while q:
                x, y = q.popleft()

                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]

                    if nx < 0 or ny < 0 or nx >= n or ny >= n:
                        continue
                    if visited[nx][ny]:
                        continue
                    if grid[nx][ny] == 0:
                        continue

                    visited[nx][ny] = 1
                    q.append((nx, ny))
                    land.append((nx, ny))
            return land

        # init
        n = len(grid)
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        island = []
        visited = [[0] * n for _ in range(n)]

        # seperate island bfs
        for i in range(n):
            for j in range(n):
                if visited[i][j]:
                    continue
                if grid[i][j] == 0:
                    continue
                island.append(bfs(i, j))

        # find min bridge length bfs
        bridge_length = 0
        visited = [[0] * n for _ in range(n)]
        q = deque()
        for x, y in island[0]:
            q.append((x, y))
            visited[x][y] = 1

        while q:
            x, y = q.popleft()

            if visited[x][y] > 1 and grid[x][y] == 1:
                bridge_length = visited[x][y] - 2  # bridge length
                break

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or ny < 0 or nx >= n or ny >= n:
                    continue
                if visited[nx][ny]:
                    continue

                q.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1

        return bridge_length
