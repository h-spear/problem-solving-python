# https://leetcode.com/problems/surrounded-regions/

from collections import deque


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        m = len(board)
        n = len(board[0])
        visited = [[0] * n for _ in range(m)]
        checker = {}

        def bfs(x, y, num):
            q = deque([(x, y)])
            visited[x][y] = num
            flag = True
            while q:
                x, y = q.popleft()

                if x == 0 or y == 0 or x == m - 1 or y == n - 1:
                    flag = False

                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]

                    if nx < 0 or ny < 0 or nx >= m or ny >= n:
                        continue
                    if visited[nx][ny]:
                        continue
                    if board[nx][ny] == "X":
                        continue

                    visited[nx][ny] = num
                    q.append((nx, ny))
            checker[num] = flag

        num = 0
        for i in range(m):
            for j in range(n):
                if visited[i][j]:
                    continue
                if board[i][j] == "X":
                    continue
                num += 1
                bfs(i, j, num)

        for i in range(m):
            for j in range(n):
                if board[i][j] == "X":
                    continue
                if checker[visited[i][j]]:
                    board[i][j] = "X"
