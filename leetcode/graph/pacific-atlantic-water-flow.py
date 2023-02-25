# https://leetcode.com/problems/pacific-atlantic-water-flow/

from collections import deque


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])
        dp = [[0] * n for _ in range(m)]
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]

        def bfs(sx, sy):
            visited = [[0] * n for _ in range(m)]
            visited[sx][sy] = 1
            q = deque([(sx, sy)])
            while q:
                x, y = q.popleft()

                if dp[x][y] == 3:
                    return
                if x == 0 or y == 0:
                    dp[sx][sy] |= 1
                if x == m - 1 or y == n - 1:
                    dp[sx][sy] |= 2

                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]

                    if nx < 0 or ny < 0 or nx >= m or ny >= n:
                        continue
                    if heights[nx][ny] > heights[x][y]:
                        continue
                    if dp[nx][ny] == 3:
                        dp[sx][sy] = 3
                        return
                    if dp[nx][ny] == 1:
                        dp[sx][sy] |= 1
                        continue
                    if dp[nx][ny] == 2:
                        dp[sx][sy] |= 2
                        continue
                    if visited[nx][ny]:
                        continue

                    visited[nx][ny] = 1
                    q.append((nx, ny))

            return

        answer = []
        for i in range(m):
            for j in range(n):
                bfs(i, j)
                if dp[i][j] == 3:
                    answer.append([i, j])

        return answer
