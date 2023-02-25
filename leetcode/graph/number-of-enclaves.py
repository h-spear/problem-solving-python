# https://leetcode.com/problems/number-of-enclaves/

from collections import deque


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        def bfs(x, y):
            visited[x][y] = 1
            q = deque([(x, y)])
            cnt = 1
            flag = True
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
                    if not grid[nx][ny]:
                        continue

                    q.append((nx, ny))
                    visited[nx][ny] = 1
                    cnt += 1

            if flag:
                return cnt
            return 0

        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
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
                answer += bfs(i, j)

        return answer
