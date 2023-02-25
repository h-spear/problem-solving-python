# https://leetcode.com/problems/island-perimeter/


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        def count_adj(x, y):
            count = 0
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or ny < 0 or nx >= row or ny >= col:
                    continue
                if grid[nx][ny]:
                    count += 1
            return count

        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        row = len(grid)
        col = len(grid[0])
        answer = 0

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 0:
                    continue
                count = count_adj(i, j)
                answer += 4 - count

        return answer
