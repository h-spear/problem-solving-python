# https://leetcode.com/problems/flood-fill/

from collections import deque


class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        m = len(image)
        n = len(image[0])
        q = deque()
        new_image = [[0] * n for _ in range(m)]
        visited = [[0] * n for _ in range(m)]

        org_color = image[sr][sc]
        if image[sr][sc] != color:
            image[sr][sc] = color
            q.append((sr, sc))
            visited[sr][sc] = 1

        while q:
            x, y = q.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or ny < 0 or nx >= m or ny >= n:
                    continue
                if visited[nx][ny]:
                    continue
                if image[nx][ny] != org_color:
                    continue

                visited[nx][ny] = 1
                q.append((nx, ny))

        for i in range(m):
            for j in range(n):
                if visited[i][j]:
                    new_image[i][j] = color
                else:
                    new_image[i][j] = image[i][j]

        return new_image
