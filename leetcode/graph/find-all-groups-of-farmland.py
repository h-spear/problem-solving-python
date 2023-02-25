# https://leetcode.com/problems/find-all-groups-of-farmland/

from collections import deque


class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        m = len(land)
        n = len(land[0])
        visited = [[0] * n for _ in range(m)]
        dx = [1, 0]
        dy = [0, 1]

        def bfs(x, y):
            visited[x][y] = 1
            q = deque([(x, y)])
            srt = (x, y)
            trg = (x, y)
            while q:
                x, y = q.popleft()

                for i in range(2):
                    nx = x + dx[i]
                    ny = y + dy[i]

                    if nx < 0 or ny < 0 or nx >= m or ny >= n:
                        continue
                    if visited[nx][ny]:
                        continue
                    if land[nx][ny] == 0:
                        continue
                    visited[nx][ny] = 1
                    trg = max(trg, (nx, ny))
                    q.append((nx, ny))

            return (*srt, *trg)

        answer = []
        for i in range(m):
            for j in range(n):
                if visited[i][j]:
                    continue
                if land[i][j] == 0:
                    continue
                answer.append(bfs(i, j))

        return answer
