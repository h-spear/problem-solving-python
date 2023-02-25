# https://leetcode.com/problems/01-matrix/

from collections import deque


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        q = deque()
        visited = [[-1] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    q.append((i, j))
                    visited[i][j] = 0

        while q:
            x, y = q.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or ny < 0 or nx >= m or ny >= n:
                    continue
                if visited[nx][ny] != -1:
                    continue

                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))

        return visited
