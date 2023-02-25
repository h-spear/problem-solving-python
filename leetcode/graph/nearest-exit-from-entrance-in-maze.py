# https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/
# dijkstra

import heapq


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        INF = float("inf")
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        m = len(maze)
        n = len(maze[0])
        sx, sy = entrance
        distance = [[INF] * n for _ in range(m)]
        distance[sx][sy] = 0
        heap = []
        heapq.heappush(heap, (0, sx, sy))
        exit = []
        answer = INF

        # find exit cell
        for j in range(n):
            if maze[0][j] == ".":
                exit.append((0, j))
            if maze[m - 1][j] == ".":
                exit.append((m - 1, j))

        for i in range(m):
            if maze[i][0] == ".":
                exit.append((i, 0))
            if maze[i][n - 1] == ".":
                exit.append((i, n - 1))

        # dijkstra
        while heap:
            dist, x, y = heapq.heappop(heap)

            if distance[x][y] < dist:
                continue

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or ny < 0 or nx >= m or ny >= n:
                    continue
                if maze[nx][ny] == "+":
                    continue

                cost = dist + 1
                if cost < distance[nx][ny]:
                    distance[nx][ny] = cost
                    heapq.heappush(heap, (cost, nx, ny))

        distance[sx][sy] = INF
        for x, y in exit:
            answer = min(distance[x][y], answer)

        if answer == INF:
            return -1
        return answer
