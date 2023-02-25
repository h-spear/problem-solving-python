# https://leetcode.com/problems/where-will-the-ball-fall/


class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m = len(grid)
        n = len(grid[0])

        answer = [-1] * n

        def down(i, j, num):
            if i == m:
                answer[num] = j
                return

            if j + 1 < n and grid[i][j] == 1 and grid[i][j + 1] == 1:
                down(i + 1, j + 1, num)
            if j - 1 >= 0 and grid[i][j] == -1 and grid[i][j - 1] == -1:
                down(i + 1, j - 1, num)

        for j in range(n):
            down(0, j, j)
        return answer
