# https://leetcode.com/problems/count-sub-islands/

from collections import deque


class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        def bfs_labeling_grid1(x, y, label):
            visited1[x][y] = label
            q = deque([(x, y)])
            while q:
                x, y = q.popleft()

                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]

                    if nx < 0 or ny < 0 or nx >= n or ny >= m:
                        continue
                    if visited1[nx][ny]:
                        continue
                    if not grid1[nx][ny]:
                        continue

                    visited1[nx][ny] = label
                    q.append((nx, ny))

        def bfs_check_grid2(x, y):
            labels = set()
            visited2[x][y] = 1
            q = deque([(x, y)])
            while q:
                x, y = q.popleft()

                labels.add(visited1[x][y])

                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]

                    if nx < 0 or ny < 0 or nx >= n or ny >= m:
                        continue
                    if visited2[nx][ny]:
                        continue
                    if not grid2[nx][ny]:
                        continue

                    visited2[nx][ny] = 1
                    q.append((nx, ny))

            if len(labels) != 1:
                return 0
            if 0 in labels:
                return 0
            return 1

        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        n = len(grid1)
        m = len(grid1[0])
        visited1 = [[0] * m for _ in range(n)]
        visited2 = [[0] * m for _ in range(n)]
        label = 1
        answer = 0

        # grid1 labeling
        for i in range(n):
            for j in range(m):
                if visited1[i][j]:
                    continue
                if not grid1[i][j]:
                    continue
                bfs_labeling_grid1(i, j, label)

        # grid2 check
        for i in range(n):
            for j in range(m):
                if visited2[i][j]:
                    continue
                if not grid2[i][j]:
                    continue
                answer += bfs_check_grid2(i, j)

        return answer
