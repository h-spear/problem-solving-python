# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/

# dfs + memorization
# Runtime: 442 ms, faster than 95.56% of Python3 online submissions for Longest Increasing Path in a Matrix.
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        def dfs(x, y):
            if dp[x][y]:
                return dp[x][y]

            temp = 0
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or ny < 0 or nx >= m or ny >= n:
                    continue
                if matrix[nx][ny] <= matrix[x][y]:
                    continue
                temp = max(temp, dfs(nx, ny))

            dp[x][y] = 1 + temp
            return dp[x][y]

        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        answer = 0

        for i in range(m):
            for j in range(n):
                answer = max(answer, dfs(i, j))

        return answer


# bfs
# Runtime: 8285 ms
from collections import deque


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        dp = [[-1] * n for _ in range(m)]
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        answer = 0

        def bfs(x, y):
            if dp[x][y] != -1:
                return

            q = deque([(x, y)])
            dp[x][y] = 1
            while q:
                x, y = q.popleft()

                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]

                    if nx < 0 or ny < 0 or nx >= m or ny >= n:
                        continue
                    if matrix[nx][ny] >= matrix[x][y]:
                        continue
                    if dp[nx][ny] >= dp[x][y] + 1:
                        continue

                    q.append((nx, ny))
                    dp[nx][ny] = dp[x][y] + 1

        for i in range(m):
            for j in range(n):
                bfs(i, j)

        for i in range(m):
            for j in range(n):
                answer = max(answer, dp[i][j])
        return answer
